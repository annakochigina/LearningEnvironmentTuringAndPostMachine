import tkinter
import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk

import const.text as text
from classes.MyOptionMenu import MyOptionMenu
from classes.PostAlg import PostAlg
from classes.ObjPostAlg import ObjPostAlg
import re
import json, random
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from pathlib import Path

TRAINER = text.CONST_TRAINER_POST


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def return_window_for_algorithms(dict_windows):
    if messagebox.askokcancel("Выход из тренажёра", "Вы уверены, что хотите выйти из тренажёра?",
                               parent=dict_windows["window_machine_post"]):
        dict_windows["window_machine_post"].destroy()
        dict_windows["window_for_algorithms"].deiconify()


def create_machine_post(dict_windows):
    window_machine_post = Tk.Tk()
    window_machine_post_width_center = (window_machine_post.winfo_screenwidth()) // 2 - 600
    window_machine_post_height_center = (window_machine_post.winfo_screenheight()) // 2 - 375
    window_machine_post.geometry(
        "1200x750+{}+{}".format(window_machine_post_width_center, window_machine_post_height_center))
    window_machine_post.config(bg="white")
    dict_windows["window_machine_post"] = window_machine_post
    window_machine_post.title("Тренажёр - машина Поста")

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_machine_post)
    label_exit = Tk.Label(window_machine_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_machine_post, image=photo_exit, background="white", relief="flat", width=40,
                            height=40, cursor="hand2", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    simulator_post_machine(dict_windows)


def save_expression(post_alg_obj, post_alg_wid):
    post_alg_wid.last_save_inf_tape = post_alg_wid.infinity_tape.copy()

    max_ind, min_ind = max(post_alg_wid.infinity_tape.keys()), min(post_alg_wid.infinity_tape.keys())
    expression = {}
    for i in range(min_ind, max_ind + 1):
        expression[i] = str(post_alg_wid.infinity_tape[i].selected_value.get())

    post_alg_obj.set_expression(expression)

    post_alg_obj.last_save_expression = post_alg_obj.expression.copy()

    post_alg_obj.last_save_pointer_index = post_alg_obj.pointer_index
    min_ind, max_ind = post_alg_wid.output_elm_ids[0], post_alg_wid.output_elm_ids[1]
    post_alg_wid.last_save_output_elm = [min_ind, max_ind]


def save_start_expression(post_alg_obj, post_alg_wid):
    post_alg_wid.start_inf_tape = post_alg_wid.infinity_tape.copy()

    max_ind, min_ind = max(post_alg_wid.infinity_tape.keys()), min(post_alg_wid.infinity_tape.keys())
    expression = {}
    for i in range(min_ind, max_ind + 1):
        expression[i] = str(post_alg_wid.infinity_tape[i].selected_value.get())

    post_alg_obj.set_expression(expression)

    post_alg_obj.start_expression = post_alg_obj.expression.copy()

    post_alg_obj.start_pointer_index = post_alg_obj.pointer_index
    min_ind, max_ind = post_alg_wid.output_elm_ids[0], post_alg_wid.output_elm_ids[1]
    post_alg_wid.start_output_elm = [min_ind, max_ind]


def read_example(post_alg_obj, post_alg_wid, dict_windows):
    filename = fd.askopenfilename(title="Открыть файл", initialdir="./EXAMPLES_POST",
                                  filetypes=(("Post Examples", "*.post"),), parent=dict_windows["window_machine_post"])

    if not filename:
        return

    cleaning_widgets(post_alg_obj, post_alg_wid)

    with open(filename, encoding='utf-8') as f:
        example_info = json.load(f)

    counter_command = example_info.get("counter_command")
    pointer_index = example_info.get("pointer_index")
    table_rules = example_info.get("table_rules")
    expression_info = example_info.get("expression")
    task_condition = example_info.get("task_condition")
    alphabetical_size = example_info.get("alphabetical_size")

    post_alg_wid.text_task_condition.delete("1.0", "end")
    post_alg_wid.text_task_condition.insert("end", task_condition)

    post_alg_obj.table_rules = [[] for i in range(counter_command)]
    post_alg_obj.pointer_index = pointer_index

    changing_alphabet(post_alg_obj, post_alg_wid, alphabetical_size, False)
    fill_rules_table(post_alg_obj, table_rules)
    for elem in post_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    post_alg_wid.list_label_ind.clear()
    delete_option_menu_from_frame(post_alg_wid.frame_infinity_tape)

    creating_and_fill_infinity_tape(post_alg_obj, post_alg_wid, expression_info, pointer_index)


def save_file(post_alg_obj, post_alg_wid, dict_windows):
    table_rules_dict = {}

    for index, rules in enumerate(post_alg_obj.table_rules):
        current_list_rules = []

        for item in rules:
            current_list_rules.append(item.get())

        table_rules_dict[str(index)] = current_list_rules

    expression = {}

    for key in post_alg_wid.infinity_tape:
        expression[str(key)] = post_alg_wid.infinity_tape[key].selected_value.get()

    example_info = {
        "alphabetical_size": len(post_alg_obj.alphabetical),
        "task_condition": post_alg_wid.text_task_condition.get("1.0", "end"),
        "counter_command": len(post_alg_obj.table_rules),
        "pointer_index": post_alg_obj.pointer_index,
        "table_rules": table_rules_dict,
        "expression": expression
    }

    new_file_example = fd.asksaveasfile(mode='w', defaultextension='.post', filetypes=(("Post Examples", "*.post"),),
                                        parent=dict_windows["window_machine_post"])

    if new_file_example:
        with open(new_file_example.name, 'w', encoding='utf-8') as f:
            json.dump(example_info, f, ensure_ascii=False, indent=4)


def tape_recovery(post_alg_obj, post_alg_wid):
    delete_option_menu_from_frame(post_alg_wid.frame_infinity_tape)
    post_alg_wid.infinity_tape.clear()

    post_alg_obj.pointer_index = post_alg_obj.last_save_pointer_index
    post_alg_wid.infinity_tape = post_alg_wid.last_save_inf_tape.copy()

    for key in post_alg_wid.infinity_tape:
        if key in post_alg_obj.last_save_expression:
            post_alg_wid.infinity_tape[key].selected_value.set(post_alg_obj.last_save_expression[key])
        else:
            post_alg_wid.infinity_tape[key].selected_value.set(" ")

    min_ind, max_ind = post_alg_wid.last_save_output_elm[0], post_alg_wid.last_save_output_elm[1]
    post_alg_wid.output_elm_ids = [min_ind, max_ind]

    place_x = 0
    i = 0
    for ind in range(post_alg_wid.output_elm_ids[0], post_alg_wid.output_elm_ids[1] + 1):
        post_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        post_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        post_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60

    if post_alg_obj.alphabetical != post_alg_wid.infinity_tape[post_alg_wid.output_elm_ids[0]].alphabetical:
        print("алфавиты не совпадают")
        post_alg_obj.alphabetical = post_alg_wid.infinity_tape[post_alg_wid.output_elm_ids[0]].alphabetical

        delete_table_rules(post_alg_obj)
        post_alg_obj.table_rules = [[] for i in range(11)]
        creating_rules_table(post_alg_obj, post_alg_wid)


def start_tape_recovery(post_alg_obj, post_alg_wid):
    delete_option_menu_from_frame(post_alg_wid.frame_infinity_tape)
    post_alg_wid.infinity_tape.clear()

    post_alg_obj.pointer_index = post_alg_obj.start_pointer_index
    post_alg_wid.infinity_tape = post_alg_wid.start_inf_tape.copy()

    for key in post_alg_wid.infinity_tape:
        if key in post_alg_obj.start_expression:
            post_alg_wid.infinity_tape[key].selected_value.set(post_alg_obj.start_expression[key])
        else:
            post_alg_wid.infinity_tape[key].selected_value.set(" ")

    min_ind, max_ind = post_alg_wid.start_output_elm[0], post_alg_wid.start_output_elm[1]
    post_alg_wid.output_elm_ids = [min_ind, max_ind]

    place_x = 0
    i = 0
    for ind in range(post_alg_wid.output_elm_ids[0], post_alg_wid.output_elm_ids[1] + 1):
        post_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        post_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        post_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def delete_option_menu_from_frame(frame: Tk.Frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tkinter.OptionMenu):
            widget.place(x=-1000, y=-1000)


def check_validate_command_bin(newval):
    return re.match("^[0-1.?<>]?$", newval) is not None


def check_validate_command_ter(newval):
    return re.match("^[0-1.?<>X]?$", newval) is not None


def check_validate_trans(newval):
    return re.match("^[0-9,]*$", newval) is not None


def creating_rules_table(post_alg_obj, post_alg_wid):
    list_entry_heading = ['Команда', 'Переход', 'Комментарии']
    if post_alg_obj.alphabet_size == 2:
        check_command = (post_alg_wid.frame_table_rules.register(check_validate_command_bin), "%P")
    elif post_alg_obj.alphabet_size == 3:
        check_command = (post_alg_wid.frame_table_rules.register(check_validate_command_ter), "%P")
    check_trans = (post_alg_wid.frame_table_rules.register(check_validate_trans), "%P")
    for i in range(len(post_alg_obj.table_rules) + 1):  # создание таблицы правил
        for j in range(4):
            cell = Tk.Entry(master=post_alg_wid.frame_table_rules, width=16, font=('Arial', "16", 'bold', "italic"),
                            relief="raised", justify='center')
            if j == 0 and i > 0:
                cell.insert("end", i)
                cell["state"] = "disabled"
                cell["width"] = 3
                post_alg_obj.list_number_row.append(cell)
            elif i == 0 and j > 0:
                cell.insert("end", list_entry_heading[j - 1])
                cell["state"] = "disabled"
            elif i == 0 and j == 0:
                cell["state"] = "disabled"
                cell["width"] = 3
            elif i > 0 and j > 0:
                post_alg_obj.table_rules[i - 1].append(cell)
                cell["validate"] = "key"
                if j == 1:
                    cell["validatecommand"] = check_command
                elif j == 2:
                    cell["validatecommand"] = check_trans
            if j == 3:
                cell["width"] = 55
            cell.grid(row=i, column=j)


def fill_rules_table(post_alg_obj, rules_table):
    for i in range(0, len(post_alg_obj.table_rules)):

        current_rules_list = rules_table.get(str(i))

        if current_rules_list:
            for index, cell in enumerate(post_alg_obj.table_rules[i]):
                cell.insert("end", current_rules_list[index])


def movement_right(post_alg_obj, post_alg_wid):
    max_ind = max(post_alg_wid.infinity_tape.keys())

    if not post_alg_wid.infinity_tape.get(post_alg_wid.output_elm_ids[1] + 1):
        symbol = Tk.StringVar(post_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        new_option_menu = Tk.OptionMenu(post_alg_wid.frame_infinity_tape, symbol, *post_alg_obj.alphabetical)
        new_my_option_menu = MyOptionMenu(new_option_menu, symbol, post_alg_obj.alphabetical)

        post_alg_wid.infinity_tape[max_ind + 1] = new_my_option_menu

    post_alg_wid.hide_left_elm_post()

    post_alg_obj.pointer_index += 1
    post_alg_wid.output_elm_ids[0] += 1
    post_alg_wid.output_elm_ids[1] += 1

    place_x = 0

    i = 0

    for ind in range(post_alg_wid.output_elm_ids[0], post_alg_wid.output_elm_ids[1] + 1):
        post_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        post_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        post_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def movement_left(post_alg_obj, post_alg_wid):
    min_ind = min(post_alg_wid.infinity_tape.keys())

    if not post_alg_wid.infinity_tape.get(post_alg_wid.output_elm_ids[0] - 1):
        symbol = Tk.StringVar(post_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        new_option_menu = Tk.OptionMenu(post_alg_wid.frame_infinity_tape, symbol, *post_alg_obj.alphabetical)
        new_my_option_menu = MyOptionMenu(new_option_menu, symbol, post_alg_obj.alphabetical)

        post_alg_wid.infinity_tape[min_ind - 1] = new_my_option_menu

    post_alg_wid.hide_right_elm_post()

    post_alg_obj.pointer_index -= 1
    post_alg_wid.output_elm_ids[0] -= 1
    post_alg_wid.output_elm_ids[1] -= 1

    place_x = 0

    i = 0

    for ind in range(post_alg_wid.output_elm_ids[0], post_alg_wid.output_elm_ids[1] + 1):
        post_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        post_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        post_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def step_alg(post_alg_obj, post_alg_wid):
    current_command = post_alg_obj.get_current_command()
    current_transition = post_alg_obj.get_current_transition()

    if current_command == "":
        messagebox.showerror(title="Ошибка", message=f"Нет команды в ячейке с номером {post_alg_obj.number_str}",
                             parent=post_alg_wid.frame_table_rules)
        return True, True

    if current_command != "?" and "," in current_transition:
        messagebox.showerror(title="Ошибка",
                             message=f"В команде «{current_command}» указывается только один адрес перехода без запятых",
                             parent=post_alg_wid.frame_table_rules)
        return True, True

    if current_command != "?" and current_command != ".":
        if current_transition != "":
            post_alg_obj.number_str = int(current_transition)
        else:
            post_alg_obj.number_str += 1

    if current_command == ">":
        movement_right(post_alg_obj, post_alg_wid)
    elif current_command == "<":
        movement_left(post_alg_obj, post_alg_wid)
    elif current_command == "0":
        if post_alg_obj.alphabet_size == 2:
            post_alg_obj.set_val_for_cur_elem(" ", post_alg_wid)
        else:
            post_alg_obj.set_val_for_cur_elem("0", post_alg_wid)
    elif current_command == "1":
        if post_alg_obj.alphabet_size == 2:
            post_alg_obj.set_val_for_cur_elem(u'\u2714', post_alg_wid)
        else:
            post_alg_obj.set_val_for_cur_elem("1", post_alg_wid)
    elif current_command == "?":
        if post_alg_obj.alphabet_size == 2:
            if "," not in current_transition or current_transition.count(",") > 1:
                messagebox.showerror(title="Ошибка",
                                     message="В команде «?» нужно указать два адреса перехода через запятую",
                                     parent=post_alg_wid.frame_table_rules)
                return True, True
            n, m = map(int, current_transition.split(","))
            value = post_alg_obj.expression[post_alg_obj.pointer_index]
            if value == " ":
                post_alg_obj.number_str = n
            elif value == u'\u2714':
                post_alg_obj.number_str = m
        else:
            if "," not in current_transition or current_transition.count(",") != 2:
                messagebox.showerror(title="Ошибка",
                                     message="В команде «?» нужно указать три адреса перехода через запятую",
                                     parent=post_alg_wid.frame_table_rules)
                return True, True
            n, m, k = map(int, current_transition.split(","))
            value = post_alg_obj.expression[post_alg_obj.pointer_index]
            if value == " ":
                post_alg_obj.number_str = n
            elif value == "0":
                post_alg_obj.number_str = m
            else:
                post_alg_obj.number_str = k
    elif current_command == "X":
        post_alg_obj.set_val_for_cur_elem(" ", post_alg_wid)
    elif current_command == ".":
        return True, False

    if post_alg_obj.number_str > len(post_alg_obj.table_rules):
        messagebox.showerror(title="Ошибка", message=f"Переход на несуществующую строку {post_alg_obj.number_str}",
                             parent=post_alg_wid.frame_table_rules)
        return True, True
    else:
        post_alg_obj.color_current_command()
    return False, False


def stop_process(post_alg_obj, post_alg_wid):
    messagebox.showinfo(title="Информация", message="Программа остановлена пользователем",
                        parent=post_alg_wid.frame_table_rules)
    post_alg_obj.stop_algorithm = False
    post_alg_obj.number_str = 1
    post_alg_obj.counter_step = -1
    post_alg_obj.stop_process = True
    for lst in post_alg_obj.table_rules:
        for cell in lst:
            cell["background"] = 'white'

    post_alg_wid.button_run["state"] = "normal"
    post_alg_wid.button_step["state"] = "normal"


def step_process_post_alg(post_alg_obj, post_alg_wid):
    print("Шаг", post_alg_obj.counter_step, "-", post_alg_obj.number_str)

    post_alg_obj.stop_algorithm = False
    post_alg_wid.button_run["state"] = "disabled"

    max_ind, min_ind = max(post_alg_wid.infinity_tape.keys()), min(post_alg_wid.infinity_tape.keys())

    expression = {}

    for i in range(min_ind, max_ind):
        expression[i] = str(post_alg_wid.infinity_tape[i].selected_value.get())

    post_alg_obj.set_expression(expression)

    if not post_alg_obj.stop_algorithm:
        if post_alg_obj.counter_step == -1:
            print("я делаю фейк шаг")
            post_alg_obj.color_current_command()
        else:
            post_alg_obj.stop_algorithm, post_alg_obj.completed_error = step_alg(post_alg_obj, post_alg_wid)

        post_alg_obj.counter_step += 1

    if post_alg_obj.stop_algorithm:

        post_alg_wid.button_run["state"] = "normal"

        post_alg_obj.number_str = 1
        post_alg_obj.counter_step = -1

        for lst in post_alg_obj.table_rules:
            for cell in lst:
                cell["background"] = 'white'

        if post_alg_obj.completed_error == False and post_alg_obj.stop_process == False:
            messagebox.showinfo(title="Информация", message="Выполнение программы завершено",
                                parent=post_alg_wid.frame_table_rules)
        post_alg_obj.stop_process = False
        post_alg_obj.completed_error = False


def process_post_alg(post_alg_obj, post_alg_wid):
    post_alg_obj.stop_process = False
    post_alg_obj.stop_algorithm = False
    save_start_expression(post_alg_obj, post_alg_wid)

    post_alg_wid.button_run["state"] = "disabled"
    post_alg_wid.button_step["state"] = "disabled"

    while not post_alg_obj.stop_algorithm:
        print(post_alg_obj.counter_step)
        if post_alg_obj.counter_step >= 1000:
            messagebox.showwarning(title="Предупреждение",
                                   message="В вашем алгоритме обнаружено больше 1000 шагов. Возможно в нем присутствует цикл. Пожалуйста, исправьте ваши правила.",
                                   parent=post_alg_wid.frame_table_rules)
            start_tape_recovery(post_alg_obj, post_alg_wid)
            post_alg_obj.completed_error = True
            break

        if post_alg_obj.stop_process:
            messagebox.showinfo(title="Информация", message="Программа остановлена пользователем",
                                parent=post_alg_wid.frame_table_rules)
            post_alg_obj.post_alg_obj.completed_error = True
            break

        max_ind, min_ind = max(post_alg_wid.infinity_tape.keys()), min(post_alg_wid.infinity_tape.keys())

        table_of_rules, expression = post_alg_obj.table_rules, {}

        for i in range(min_ind, max_ind):
            expression[i] = str(post_alg_wid.infinity_tape[i].selected_value.get())

        post_alg_obj.set_expression(expression)

        post_alg_obj.stop_algorithm, post_alg_obj.completed_error = step_alg(post_alg_obj, post_alg_wid)
        post_alg_obj.counter_step += 1

    if post_alg_obj.completed_error == False:
        messagebox.showinfo(title="Информация", message="Выполнение программы завершено",
                            parent=post_alg_wid.frame_table_rules)
    post_alg_obj.number_str = 1
    post_alg_wid.button_run["state"] = "normal"
    post_alg_wid.button_step["state"] = "normal"

    for lst in post_alg_obj.table_rules:
        for cell in lst:
            cell["background"] = 'white'

    post_alg_obj.completed_error = False
    post_alg_obj.counter_step = -1


def add_row_table_rules(post_alg_obj, post_alg_wid):
    lst = []
    i = len(post_alg_obj.table_rules) + 1
    if post_alg_obj.alphabet_size == 2:
        check_command = (post_alg_wid.frame_table_rules.register(check_validate_command_bin), "%P")
    elif post_alg_obj.alphabet_size == 3:
        check_command = (post_alg_wid.frame_table_rules.register(check_validate_command_ter), "%P")
    check_trans = (post_alg_wid.frame_table_rules.register(check_validate_trans), "%P")
    for j in range(4):
        cell = Tk.Entry(master=post_alg_wid.frame_table_rules, width=16, font=('Arial', 16, 'bold'), relief="raised",
                        justify='center', )
        if j == 0:
            cell.insert("end", i)
            cell["state"] = "disabled"
            cell["width"] = 3
            post_alg_obj.list_number_row.append(cell)
        else:
            lst.append(cell)
            cell["validate"] = "key"
            if j == 1:
                cell["validatecommand"] = check_command
            elif j == 2:
                cell["validatecommand"] = check_trans
            if j == 3:
                cell["width"] = 55
        cell.grid(row=i, column=j)

    post_alg_obj.table_rules.append(lst)


def delete_row_table_rules(post_alg_obj, post_alg_wid):
    if len(post_alg_obj.table_rules) <= 1:
        return

    cell = post_alg_obj.list_number_row[-1]
    cell.destroy()
    post_alg_obj.list_number_row.pop()

    while len(post_alg_obj.table_rules[-1]) != 0:
        cell = post_alg_obj.table_rules[-1][-1]
        cell.destroy()
        post_alg_obj.table_rules[-1].pop()
    post_alg_obj.table_rules.pop()


def creating_infinity_tape(post_alg_obj, post_alg_wid):
    place_x = 0
    post_alg_obj.pointer_index = 0

    for ind in range(-9, 10):
        symbol = Tk.StringVar(post_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        current_opt_menu = Tk.OptionMenu(post_alg_wid.frame_infinity_tape, symbol, *post_alg_obj.alphabetical)
        current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        current_opt_menu.place(x=place_x, y=63, width=60, height=40)
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, post_alg_obj.alphabetical)
        post_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=post_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"))
        lbl.place(x=place_x + 20, y=44)
        post_alg_wid.list_label_ind.append(lbl)

        place_x += 60


def creating_and_fill_infinity_tape(post_alg_obj, post_alg_wid, expression_info, pointer_index):
    place_x = 0
    post_alg_obj.pointer_index = pointer_index

    min_ind, max_ind = min(expression_info.keys()), max(expression_info.keys())
    min_ind, max_ind = min([int(min_ind), pointer_index - 9]), max([int(max_ind), pointer_index + 10])
    print(f"min {min_ind} and max {max_ind}")

    post_alg_wid.output_elm_ids = [pointer_index - 9, pointer_index + 10]
    print(post_alg_wid.output_elm_ids)

    for ind in range(min_ind, max_ind + 1):
        symbol = Tk.StringVar(post_alg_wid.frame_infinity_tape)
        symbol.set(expression_info.get(str(ind), " "))

        current_opt_menu = Tk.OptionMenu(post_alg_wid.frame_infinity_tape, symbol, *post_alg_obj.alphabetical)
        current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, post_alg_obj.alphabetical)
        post_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=post_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"))

        if post_alg_wid.output_elm_ids[0] <= ind <= post_alg_wid.output_elm_ids[1]:
            current_opt_menu.place(x=place_x, y=60, width=60, height=40)
            lbl.place(x=place_x + 20, y=40)
            place_x += 60
            post_alg_wid.list_label_ind.append(lbl)


def delete_table_rules(post_alg_obj):
    for elem in post_alg_obj.list_number_row:
        cell = elem
        cell.destroy()
    post_alg_obj.list_number_row.clear()

    for lst in post_alg_obj.table_rules:
        for elem in lst:
            cell = elem
            cell.destroy()
    post_alg_obj.table_rules.clear()


def cleaning_widgets(post_alg_obj, post_alg_wid):
    delete_table_rules(post_alg_obj)

    for elem in post_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    post_alg_wid.list_label_ind.clear()

    if post_alg_wid.tests:
        post_alg_wid.tests.destroy()

    post_alg_obj.table_rules = [[] for i in range(11)]

    post_alg_wid.output_elm_ids = [-9, 9]

    delete_option_menu_from_frame(post_alg_wid.frame_infinity_tape)


def changing_alphabet(post_alg_obj, post_alg_wid, var, need_cleaning=True):
    post_alg_obj.alphabetical = []
    post_alg_obj.alphabet_size = var
    if post_alg_obj.alphabet_size == 2:
        post_alg_obj.alphabetical = [" ", u'\u2714']
    elif post_alg_obj.alphabet_size == 3:
        post_alg_obj.alphabetical = [" ", "0", "1"]

    if need_cleaning:
        cleaning_widgets(post_alg_obj, post_alg_wid)

    creating_rules_table(post_alg_obj, post_alg_wid)
    creating_infinity_tape(post_alg_obj, post_alg_wid)


def creating_new_file(post_alg_obj, post_alg_wid):
    post_alg_wid.text_task_condition.delete("1.0", "end")  # очищение условия задачи

    cleaning_widgets(post_alg_obj, post_alg_wid)  # очищение виджетов

    creating_rules_table(post_alg_obj, post_alg_wid)
    creating_infinity_tape(post_alg_obj, post_alg_wid)


def help_trainer(dict_windows):
    window = Tk.Toplevel()
    window.title("Как работать с тренажером?")
    window_width_center = (window.winfo_screenwidth()) // 2 - 350
    window_height_center = (window.winfo_screenheight()) // 2 - 300
    window.geometry("700x650+{}+{}".format(window_width_center, window_height_center))
    window.config(background="white")
    window.resizable(width=False, height=False)

    label = Tk.Label(window, text="Как работать с тренажером?", justify="center", font=("Gabriola", "20"),
                     background="white")
    label.place(x=150, y=5)

    text = Tk.Frame(master=window, width=675, height=600, background="white")
    text.place(x=10, y=50)

    label_info = Tk.Label(master=text, text=TRAINER, justify="left", font=("Bahnschrift Light", "12"),
                          background="white")
    label_info.place(x=5, y=5)


def create_table_tests(post_alg_wid, table_tests):
    test = Tk.Frame(master=post_alg_wid.text_task_condition, background="white", border=10)
    test.place(x=15, y=45)
    post_alg_wid.tests = test

    columns = ("Входной параметр", "Результат")
    tree = ttk.Treeview(master=test, columns=columns, show="headings")
    tree.pack(fill="both", expand=1)
    tree.heading("Входной параметр", text="Входной параметр")
    tree.heading("Результат", text="Результат")

    for test in table_tests:
        tree.insert("", "end", values=test)


def first_task_laboratory_work(post_alg_wid):

    post_alg_wid.text_task_condition.delete("1.0", "end")
    if post_alg_wid.tests:
        post_alg_wid.tests.destroy()

    # генерация условия задания 1
    flag = True
    while flag:
        count_deleted_сhet = random.randint(0,3)
        count_deleted_nechet = random.randint(0,3)
        if count_deleted_сhet != count_deleted_nechet:
            flag = False
    action = random.choice(['Удалить','Добавить'])
    str_mark = ''
    if count_deleted_nechet == 0:
        str_mark = 'меток'
    elif count_deleted_nechet == 1:
        str_mark = 'метку'
    else:
        str_mark = 'метки'

    text_task = f'{action} {count_deleted_nechet} {str_mark} в середине массива, если в массиве нечетное количество меток, и ' \
                f'{count_deleted_сhet}, если четное'
    post_alg_wid.text_task_condition.insert("end", text_task)

    # генерация тестов
    table_tests = []
    test_one = random.randint(3, 7)*2
    if action == 'Удалить':
        test_one_answer = u'\u2714'*(test_one-count_deleted_сhet)
    else:
        test_one_answer = u'\u2714' * (test_one + count_deleted_сhet)
    table_tests.append(tuple([test_one, test_one_answer]))
    test_two = random.randint(3, 7) * 2 + 1
    if action == 'Удалить':
        test_two_answer = u'\u2714' * (test_two - count_deleted_nechet)
    else:
        test_two_answer = u'\u2714' * (test_two + count_deleted_nechet)
    table_tests.append(tuple([test_two, test_two_answer]))

    create_table_tests(post_alg_wid, table_tests)


def second_task_laboratory_work(post_alg_wid):
    post_alg_wid.text_task_condition.delete("1.0", "end")
    if post_alg_wid.tests:
        post_alg_wid.tests.destroy()

    # генерация условия задания 2
    divisibility_number = random.randint(2,5)

    text_task = f'Проверить, делится ли количество меток на {divisibility_number}. В конце работы рядом с сохраненным числом ' \
                f'через пробел должна появляться метка, если число делится на {divisibility_number}, иначе метка не должна появляться'
    post_alg_wid.text_task_condition.insert("end", text_task)

    table_tests = []
    flag = True
    while flag:
        test_one = random.randint(2, 10)
        test_two = random.randint(2, 10)
        if test_one != test_two and test_one % divisibility_number == 0 or test_two % divisibility_number == 1:
            flag = False

    test_one_answer = u'\u2714'*test_one + '  ' + u'\u2714'
    table_tests.append(tuple([test_one, test_one_answer]))
    test_two_answer = u'\u2714'*test_two
    table_tests.append(tuple([test_two, test_two_answer]))

    create_table_tests(post_alg_wid, table_tests)


def third_task_laboratory_work(post_alg_wid):
    post_alg_wid.text_task_condition.delete("1.0", "end")
    if post_alg_wid.tests:
        post_alg_wid.tests.destroy()

    remains_number = random.randint(2, 5)

    text_task = f'Найти остаток от деления количества меток на {remains_number}'
    post_alg_wid.text_task_condition.insert("end", text_task)

    table_tests = []
    flag = True
    while flag:
        test_one = random.randint(2, 16)
        test_two = random.randint(2, 16)
        if test_one != test_two and test_one % remains_number != 0 and test_two % remains_number != 0:
            flag = False

    test_one_answer = u'\u2714' * (test_one%remains_number)
    table_tests.append(tuple([test_one, test_one_answer]))
    test_two_answer = u'\u2714' * (test_two%remains_number)
    table_tests.append(tuple([test_two, test_two_answer]))

    create_table_tests(post_alg_wid, table_tests)


def fouth_task_laboratory_work(post_alg_wid):
    post_alg_wid.text_task_condition.delete("1.0", "end")
    if post_alg_wid.tests:
        post_alg_wid.tests.destroy()

    number_one = random.randint(1, 9)
    number_two = random.randint(1, 9)

    text_task = f'Написать программу, которая складывает два целых числа: {number_one} и {number_two}'
    post_alg_wid.text_task_condition.insert("end", text_task)

    table_tests = []
    test_one = u'\u2714'*number_one + '  ' + u'\u2714'*number_two
    test_one_answer = u'\u2714' * (number_one + number_two)
    table_tests.append(tuple([test_one, test_one_answer]))

    create_table_tests(post_alg_wid, table_tests)


def simulator_post_machine(dict_windows):
    window_machine_post = dict_windows.get("window_machine_post")

    frame_title = Tk.Frame(master=window_machine_post, width=1200, height=300, background=rgb_hack((1, 116, 64)))
    frame_title.place(x=0, y=45)

    label_task_сondition = Tk.Label(master=window_machine_post, text="Условие задачи:", height=1, justify="left",
                                    font=("Gabriola", "20"), background=rgb_hack((1, 116, 64)))
    label_task_сondition.place(x=10, y=45)
    text_task_condition = Tk.Text(master=window_machine_post, width=147, height=10)
    text_task_condition.place(x=10, y=85)

    container = ttk.Frame(master=window_machine_post, width=1100, height=360)
    canvas = Tk.Canvas(master=container, width=1100, height=350)
    scrollbary = ttk.Scrollbar(master=container, orient=Tk.VERTICAL, command=canvas.yview)

    frame_table_rules = Tk.Frame(master=canvas, width=1100, height=360, border=10, background=rgb_hack((1, 116, 64)))
    frame_table_rules.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=frame_table_rules, anchor="nw")
    canvas.configure(yscrollcommand=scrollbary.set)

    container.place(x=80, y=385, width=1120, height=360)
    canvas.pack(side="left", expand=True)

    scrollbary.pack(side="right", fill=Tk.Y)

    table_rules = [[] for i in range(11)]

    alphabetical = []
    alphabet_size = 2

    infinity_tape = {}
    output_elm_ids = [-9, 9]

    frame_infinity_tape = Tk.Frame(master=window_machine_post, width=1140, height=100, padx=0, pady=0)
    frame_infinity_tape.place(x=30, y=275)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_machine_post)
    label_point = Tk.Label(window_machine_post, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40)
    label_point.place(x=547, y=0)

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_machine_post)
    label_right = Tk.Label(window_machine_post, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_machine_post, image=photo_right, width=1, height=6,
                             command=lambda: movement_right(post_alg_obj, post_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_machine_post)
    label_left = Tk.Label(window_machine_post, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_machine_post, image=photo_left, width=1, height=6,
                            command=lambda: movement_left(post_alg_obj, post_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)

    img_run = Image.open(Path.cwd() / "Image" / "Play.png")
    photo_run = ImageTk.PhotoImage(img_run, master=window_machine_post)
    label_run = Tk.Label(window_machine_post, image=photo_run)
    label_run.image = photo_run
    button_run = Tk.Button(master=window_machine_post, text="Выполнить  ", image=photo_run, compound="right", width=150,
                           height=20, cursor="hand2", font=("Gabriola", "20"), state="normal",
                           command=lambda: process_post_alg(post_alg_obj, post_alg_wid))
    button_run.place(x=10, y=10)

    img_step = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_step = ImageTk.PhotoImage(img_step, master=window_machine_post)
    label_step = Tk.Label(window_machine_post, image=photo_step)
    label_step.image = photo_step
    button_step = Tk.Button(master=window_machine_post, text="Шаг  ", image=photo_step, compound="right", width=100,
                            height=20, cursor="hand2", font=("Gabriola", "20"), state="normal",
                            command=lambda: step_process_post_alg(post_alg_obj, post_alg_wid))
    button_step.place(x=180, y=10)

    img_stop = Image.open(Path.cwd() / "Image" / "Stop.png")
    photo_stop = ImageTk.PhotoImage(img_stop, master=window_machine_post)
    label_stop = Tk.Label(window_machine_post, image=photo_stop)
    label_stop.image = photo_stop
    button_stop = Tk.Button(master=window_machine_post, text="Остановить  ", image=photo_stop, compound="right",
                            width=150, height=20, font=("Gabriola", "20"), cursor="hand2",
                            command=lambda: stop_process(post_alg_obj, post_alg_wid))
    button_stop.place(x=300, y=10)

    img_add = Image.open(Path.cwd() / "Image" / "addrow.png")
    photo_add = ImageTk.PhotoImage(img_add, master=window_machine_post)
    label_add = Tk.Label(window_machine_post, image=photo_add)
    label_add.image = photo_add
    button_add_row = Tk.Button(master=window_machine_post, image=photo_add, width=40, height=40, background="white",
                               relief="flat", cursor="hand2", state="normal",
                               command=lambda: add_row_table_rules(post_alg_obj, post_alg_wid))
    button_add_row.place(x=15, y=385)

    img_del = Image.open(Path.cwd() / "Image" / "delrow.png")
    photo_del = ImageTk.PhotoImage(img_del, master=window_machine_post)
    label_del = Tk.Label(window_machine_post, image=photo_del)
    label_del.image = photo_del
    button_delete_row = Tk.Button(master=window_machine_post, image=photo_del, width=40, height=40, background="white",
                                  relief="flat", cursor="hand2", state="normal",
                                  command=lambda: delete_row_table_rules(post_alg_obj, post_alg_wid))
    button_delete_row.place(x=15, y=435)

    post_alg_obj = PostAlg(table_rules, alphabetical, 0, alphabet_size)
    post_alg_wid = ObjPostAlg(infinity_tape, frame_infinity_tape, output_elm_ids, text_task_condition,
                              frame_table_rules, button_right, button_left, button_run, button_step)

    changing_alphabet(post_alg_obj, post_alg_wid, 2)
    save_expression(post_alg_obj, post_alg_wid)

    # создание верхнего меню
    mainmenu = Tk.Menu(master=window_machine_post)

    filemenu = Tk.Menu(master=mainmenu, tearoff=0)
    filemenu.add_command(label="Новый", command=lambda: creating_new_file(post_alg_obj, post_alg_wid))
    filemenu.add_command(label="Открыть...", command=lambda: read_example(post_alg_obj, post_alg_wid, dict_windows))
    filemenu.add_command(label="Сохранить как ...", command=lambda: save_file(post_alg_obj, post_alg_wid, dict_windows))
    filemenu.add_separator()
    filemenu.add_command(label="Выход", command=lambda: return_window_for_algorithms(dict_windows))

    tapemenu = Tk.Menu(master=mainmenu, tearoff=0)
    tapemenu.add_command(label="Сохранить ленту", command=lambda: save_expression(post_alg_obj, post_alg_wid))
    tapemenu.add_command(label="Восстановить ленту", command=lambda: tape_recovery(post_alg_obj, post_alg_wid))

    alphabetmenu = Tk.Menu(master=mainmenu, tearoff=0)
    alphabetmenu.add_radiobutton(label="Двузначный", command=lambda: changing_alphabet(post_alg_obj, post_alg_wid, 2))
    alphabetmenu.add_radiobutton(label="Трехзначный", command=lambda: changing_alphabet(post_alg_obj, post_alg_wid, 3))

    labworkmenu = Tk.Menu(master=mainmenu, tearoff=0)
    labworkmenu.add_command(label="Задание 1", command=lambda: first_task_laboratory_work(post_alg_wid))
    labworkmenu.add_command(label="Задание 2", command=lambda: second_task_laboratory_work(post_alg_wid))
    labworkmenu.add_command(label="Задание 3", command=lambda: third_task_laboratory_work(post_alg_wid))
    labworkmenu.add_command(label="Задание 4", command=lambda: fouth_task_laboratory_work(post_alg_wid))
    # labworkmenu.add_command(label="Задание 5")

    processmenu = Tk.Menu(master=mainmenu, tearoff=0)
    processmenu.add_command(label="Запуск", command=lambda: process_post_alg(post_alg_obj, post_alg_wid))
    processmenu.add_command(label="Выполнить шаг", command=lambda: step_process_post_alg(post_alg_obj, post_alg_wid))

    helpmenu = Tk.Menu(master=mainmenu, tearoff=0)
    helpmenu.add_command(label="Как работать с тренажером", command=lambda: help_trainer(dict_windows))

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Лента", menu=tapemenu)
    mainmenu.add_cascade(label="Алфавит", menu=alphabetmenu)
    mainmenu.add_cascade(label="Лабораторная работа", menu=labworkmenu)
    mainmenu.add_cascade(label="Выполнение", menu=processmenu)

    mainmenu.add_cascade(label="?", menu=helpmenu)

    window_machine_post.config(menu=mainmenu)

    window_machine_post.protocol("WM_DELETE_WINDOW", lambda: return_window_for_algorithms(dict_windows))
