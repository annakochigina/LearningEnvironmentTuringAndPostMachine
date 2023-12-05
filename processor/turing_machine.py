import tkinter
import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk
from classes.MyOptionMenu import MyOptionMenu
from classes.TuringAlg import TuringAlg
from classes.ObjTuringAlg import ObjTuringAlg
import re, os
import const.text as text
from PIL import Image, ImageTk
from pathlib import Path

import tkinter.filedialog as fd
import json, random

TRAINER = text.CONST_TRAINER_TUR


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def return_window_for_algorithms(dict_windows):
    if (messagebox.askokcancel("Выход из тренажёра", "Вы уверены, что хотите выйти из тренажёра?",
                               parent=dict_windows["window_machine_turing"])):
        dict_windows["window_machine_turing"].destroy()
        dict_windows["window_for_algorithms"].deiconify()


def create_machine_turing(dict_windows):
    window_machine_turing = Tk.Tk()
    window_machine_turing_width_center = (window_machine_turing.winfo_screenwidth()) // 2 - 600
    window_machine_turing_height_center = (window_machine_turing.winfo_screenheight()) // 2 - 375
    window_machine_turing.geometry(
        "1200x750+{}+{}".format(window_machine_turing_width_center, window_machine_turing_height_center))
    window_machine_turing.resizable(width=False, height=False)
    window_machine_turing.config(bg="white")
    dict_windows["window_machine_turing"] = window_machine_turing
    window_machine_turing.title("Тренажёр - машина Тьюринга")

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_machine_turing)
    label_exit = Tk.Label(window_machine_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_machine_turing, image=photo_exit, relief="flat", background="white", width=40,
                            height=40, cursor="hand2", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    simulator_turing_machine(dict_windows)


def save_expression(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.last_save_inf_tape = turing_alg_wid.infinity_tape.copy()

    max_ind, min_ind = max(turing_alg_wid.infinity_tape.keys()), min(turing_alg_wid.infinity_tape.keys())
    expression = {}
    for i in range(min_ind, max_ind + 1):
        expression[i] = str(turing_alg_wid.infinity_tape[i].selected_value.get())

    turing_alg_obj.set_expression(expression)

    turing_alg_obj.last_save_expression = turing_alg_obj.expression.copy()

    turing_alg_obj.last_save_pointer_index = turing_alg_obj.pointer_index
    min_ind, max_ind = turing_alg_wid.output_elm_ids[0], turing_alg_wid.output_elm_ids[1]
    turing_alg_wid.last_save_output_elm = [min_ind, max_ind]


def save_start_expression(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.start_inf_tape = turing_alg_wid.infinity_tape.copy()

    max_ind, min_ind = max(turing_alg_wid.infinity_tape.keys()), min(turing_alg_wid.infinity_tape.keys())
    expression = {}
    for i in range(min_ind, max_ind + 1):
        expression[i] = str(turing_alg_wid.infinity_tape[i].selected_value.get())

    turing_alg_obj.set_expression(expression)

    turing_alg_obj.start_expression = turing_alg_obj.expression.copy()

    turing_alg_obj.start_pointer_index = turing_alg_obj.pointer_index
    min_ind, max_ind = turing_alg_wid.output_elm_ids[0], turing_alg_wid.output_elm_ids[1]
    turing_alg_wid.start_output_elm = [min_ind, max_ind]


def start_tape_recovery(turing_alg_obj, turing_alg_wid):
    delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
    turing_alg_wid.infinity_tape.clear()

    turing_alg_obj.pointer_index = turing_alg_obj.start_pointer_index
    turing_alg_wid.infinity_tape = turing_alg_wid.start_inf_tape.copy()

    for key in turing_alg_wid.infinity_tape:
        if key in turing_alg_obj.start_expression:
            turing_alg_wid.infinity_tape[key].selected_value.set(turing_alg_obj.start_expression[key])
        else:
            turing_alg_wid.infinity_tape[key].selected_value.set(" ")

    min_ind, max_ind = turing_alg_wid.start_output_elm[0], turing_alg_wid.start_output_elm[1]
    turing_alg_wid.output_elm_ids = [min_ind, max_ind]

    place_x = 0
    i = 0
    for ind in range(turing_alg_wid.output_elm_ids[0], turing_alg_wid.output_elm_ids[1] + 1):
        turing_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        turing_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        turing_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def tape_recovery(turing_alg_obj, turing_alg_wid):
    delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
    turing_alg_wid.infinity_tape.clear()

    turing_alg_obj.pointer_index = turing_alg_obj.last_save_pointer_index
    turing_alg_wid.infinity_tape = turing_alg_wid.last_save_inf_tape.copy()

    for key in turing_alg_wid.infinity_tape:
        if key in turing_alg_obj.last_save_expression:
            turing_alg_wid.infinity_tape[key].selected_value.set(turing_alg_obj.last_save_expression[key])
        else:
            turing_alg_wid.infinity_tape[key].selected_value.set(" ")

    min_ind, max_ind = turing_alg_wid.last_save_output_elm[0], turing_alg_wid.last_save_output_elm[1]
    turing_alg_wid.output_elm_ids = [min_ind, max_ind]

    place_x = 0
    i = 0
    for ind in range(turing_alg_wid.output_elm_ids[0], turing_alg_wid.output_elm_ids[1] + 1):
        turing_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        turing_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        turing_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60

    if turing_alg_obj.alphabetical != turing_alg_wid.infinity_tape[turing_alg_wid.output_elm_ids[0]].alphabetical:
        print("алфавиты не совпадают")
        turing_alg_obj.alphabetical = turing_alg_wid.infinity_tape[turing_alg_wid.output_elm_ids[0]].alphabetical

        delete_rules_table(turing_alg_obj)

        turing_alg_obj.counter_states = 2
        creating_rules_table(turing_alg_obj, turing_alg_wid)


def delete_option_menu_from_frame(frame: Tk.Frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tkinter.OptionMenu):
            widget.place(x=-1000, y=-1000)


def creating_infinity_tape(turing_alg_obj, turing_alg_wid):
    place_x = 0
    turing_alg_obj.pointer_index = 0

    for ind in range(-9, 10):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        current_opt_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        current_opt_menu.place(x=place_x, y=63, width=60, height=40)
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, turing_alg_obj.alphabetical)
        turing_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=turing_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"))
        lbl.place(x=place_x + 20, y=44)
        turing_alg_wid.list_label_ind.append(lbl)

        place_x += 60


def create_and_fill_infinity_tape(turing_alg_obj, turing_alg_wid, expression_info, pointer_index):
    place_x = 0

    turing_alg_obj.pointer_index = pointer_index

    min_ind, max_ind = min(expression_info.keys()), max(expression_info.keys())
    min_ind, max_ind = min([int(min_ind), pointer_index - 9]), max([int(max_ind), pointer_index + 10])
    print(f"min {min_ind} and max {max_ind}")

    turing_alg_wid.output_elm_ids = [pointer_index - 9, pointer_index + 10]

    for ind in range(min_ind, max_ind + 1):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(expression_info.get(str(ind), " "))

        current_opt_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, turing_alg_obj.alphabetical)
        turing_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=turing_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"))

        if turing_alg_wid.output_elm_ids[0] <= ind < turing_alg_wid.output_elm_ids[1]:
            current_opt_menu.place(x=place_x, y=63, width=60, height=40)
            lbl.place(x=place_x + 20, y=43)
            place_x += 60

        turing_alg_wid.list_label_ind.append(lbl)


def input_alphabet(turing_alg_obj, text_alphabetical, turing_alg_wid):
    if len(text_alphabetical) != len(set(text_alphabetical)):
        messagebox.showerror(title="Ошибка", message="Алфавит содержит повторяющиеся элементы",
                             parent=turing_alg_wid.frame_table_rules)
        return

    turing_alg_obj.alphabetical = list(set(text_alphabetical))
    turing_alg_obj.alphabetical.sort()
    if " " not in turing_alg_obj.alphabetical:
        turing_alg_obj.alphabetical.append(" ")

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    creating_infinity_tape(turing_alg_obj, turing_alg_wid)
    creating_rules_table(turing_alg_obj, turing_alg_wid)


def read_example(turing_alg_obj, turing_alg_wid, dict_windows):
    filename = fd.askopenfilename(title="Открыть файл", initialdir="./EXAMPLES_TURING",
                                  filetypes=(("Turing Examples", "*.tur"),),
                                  parent=dict_windows["window_machine_turing"])

    if not filename:
        return

    with open(filename, encoding='utf-8') as f:
        example_info = json.load(f)

    task_condition = example_info.get("task_condition")
    turing_alg_wid.text_task_condition.delete("1.0", "end")
    turing_alg_wid.text_task_condition.insert("end", task_condition)

    # if len(example_info) == 2 and example_info["task_condition"] and example_info["tests"]:
    #     test = Tk.Frame(master=turing_alg_wid.text_task_condition, background="white", border=10)
    #     test.place(x=10, y=40)
    #
    #     turing_alg_wid.tests = test
    #
    #     table_val = example_info.get("tests")
    #     table_tests = []
    #     for key in table_val:
    #         table_tests.append(tuple([key, table_val[key]]))
    #     columns = ("input", "output")
    #     tree = ttk.Treeview(master=test, columns=columns, show="headings")
    #     tree.pack(fill="both", expand=1)
    #     tree.heading("input", text="input")
    #     tree.heading("output", text="output")
    #
    #     for test in table_tests:
    #         tree.insert("", "end", values=test)
    #
    # elif len(example_info) > 1:
    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    alphabetical_text = example_info.get("alphabetical")
    counter_states = example_info.get("counter_states")
    pointer_index = example_info.get("pointer_index")
    table_rules = example_info.get("table_rules")
    expression_info = example_info.get("expression")

    turing_alg_obj.pointer_index = pointer_index
    turing_alg_obj.counter_states = counter_states

    input_alphabet(turing_alg_obj, alphabetical_text, turing_alg_wid)
    fill_rules_table(turing_alg_obj, table_rules)
    cleaning_infinity_tape(turing_alg_wid)

    create_and_fill_infinity_tape(turing_alg_obj, turing_alg_wid, expression_info, pointer_index)


def save_file(turing_alg_obj, turing_alg_wid, dict_windows):
    table_rules_dict = {}

    for key in turing_alg_obj.table_rules:
        current_list_rules = []

        for elm in turing_alg_obj.table_rules[key]:
            current_list_rules.append(elm.get())

        table_rules_dict[key] = current_list_rules

    expression = {}

    for key in turing_alg_wid.infinity_tape:
        expression[str(key)] = turing_alg_wid.infinity_tape[key].selected_value.get()

    example_info = {
        "alphabetical": "".join(turing_alg_obj.alphabetical),
        "task_condition": turing_alg_wid.text_task_condition.get("1.0", "end"),
        "counter_states": turing_alg_obj.counter_states,
        "pointer_index": turing_alg_obj.pointer_index,
        "table_rules": table_rules_dict,
        "expression": expression
    }

    new_file_example = fd.asksaveasfile(mode='w', defaultextension='.tur', filetypes=(("Turing Examples", "*.tur"),),
                                        parent=dict_windows["window_machine_turing"])

    if new_file_example:
        json.dump(example_info, new_file_example, ensure_ascii=False, indent=4)


def creating_new_file(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.text_task_condition.delete("1.0", "end")  # очищение условия задачи
    turing_alg_wid.entry_alphabetical.delete("0", "end")

    turing_alg_obj.alphabetical = ["0", "1", " "]

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    creating_infinity_tape(turing_alg_obj, turing_alg_wid)
    turing_alg_obj.counter_states = 2
    creating_rules_table(turing_alg_obj, turing_alg_wid)


def delete_rules_table(turing_alg_obj):
    for elem in turing_alg_obj.list_entry_states:
        cell = elem
        cell.destroy()
    turing_alg_obj.list_entry_states.clear()

    for elem in turing_alg_obj.list_entry_alphabet:
        cell = elem
        cell.destroy()
    turing_alg_obj.list_entry_alphabet.clear()

    for key in turing_alg_obj.table_rules:
        lst = turing_alg_obj.table_rules[key]
        for elem in lst:
            cell = elem
            cell.destroy()
    turing_alg_obj.table_rules.clear()


def cleaning_infinity_tape(turing_alg_wid):
    for elem in turing_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    turing_alg_wid.list_label_ind.clear()

    delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
    turing_alg_wid.infinity_tape.clear()


def cleaning_widgets(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.output_elm_ids = [-9, 9]

    if turing_alg_wid.tests:
        turing_alg_wid.tests.destroy()

    delete_rules_table(turing_alg_obj)

    for elem in turing_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    turing_alg_wid.list_label_ind.clear()

    delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
    turing_alg_wid.infinity_tape.clear()


def movement_right(turing_alg_obj, turing_alg_wid):
    max_ind = max(turing_alg_wid.infinity_tape.keys())

    if not turing_alg_wid.infinity_tape.get(turing_alg_wid.output_elm_ids[1] + 1):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        new_option_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        new_my_option_menu = MyOptionMenu(new_option_menu, symbol, turing_alg_obj.alphabetical)

        turing_alg_wid.infinity_tape[max_ind + 1] = new_my_option_menu

    turing_alg_wid.hide_left_elm()

    turing_alg_obj.pointer_index += 1
    turing_alg_wid.output_elm_ids[0] += 1
    turing_alg_wid.output_elm_ids[1] += 1

    place_x = 0

    i = 0
    for ind in range(turing_alg_wid.output_elm_ids[0], turing_alg_wid.output_elm_ids[1] + 1):
        turing_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        turing_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        turing_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def movement_left(turing_alg_obj, turing_alg_wid):
    min_ind = min(turing_alg_wid.infinity_tape.keys())

    if not turing_alg_wid.infinity_tape.get(turing_alg_wid.output_elm_ids[0] - 1):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        new_option_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        new_my_option_menu = MyOptionMenu(new_option_menu, symbol, turing_alg_obj.alphabetical)

        turing_alg_wid.infinity_tape[min_ind - 1] = new_my_option_menu

    turing_alg_wid.hide_right_elm()

    turing_alg_obj.pointer_index -= 1
    turing_alg_wid.output_elm_ids[0] -= 1
    turing_alg_wid.output_elm_ids[1] -= 1

    place_x = 0

    i = 0
    for ind in range(turing_alg_wid.output_elm_ids[0], turing_alg_wid.output_elm_ids[1] + 1):
        turing_alg_wid.infinity_tape[ind].option_menu.config(width=2, height=2, font=('Helvetica', 12))
        turing_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=63, width=60, height=40)

        turing_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def creating_rules_table(turing_alg_obj, turing_alg_wid):

    def check_validate_alphabetical(newval):
        check_str = f"^[{turing_alg_obj.get_alphabetical_str()}]?[<>.]?[0-{turing_alg_obj.counter_states}]*$"
        return re.match(check_str, newval) is not None

    check_alphabetical = (turing_alg_wid.frame_table_rules.register(check_validate_alphabetical), "%P")
    for i in range(len(turing_alg_obj.alphabetical) + 1):  # создание таблицы правил
        for j in range(turing_alg_obj.counter_states + 1):
            cell = Tk.Entry(master=turing_alg_wid.frame_table_rules, width=5, font=("Arial", "16", "italic", "bold"),
                            relief="raised")
            if j == 0 and i > 0:
                # if (turing_alg_obj.alphabetical[i - 1] == ' '):
                #     cell.insert("end", 'λ')
                # else: вставить знак лямбды
                cell.insert("end", turing_alg_obj.alphabetical[i - 1])
                cell["state"] = "disabled"
                cell["justify"] = "center"
                turing_alg_obj.list_entry_alphabet.append(cell)
            elif i == 0 and j > 0:
                cell.insert("end", f"Q{j}")
                cell["state"] = "disabled"
                cell["justify"] = "center"
                turing_alg_obj.list_entry_states.append(cell)
            elif i == 0 and j == 0:
                cell["state"] = "disabled"
                turing_alg_obj.list_entry_states.append(cell)
            if i > 0 and j > 0:
                cell["validate"] = "key"
                cell["validatecommand"] = check_alphabetical
                if turing_alg_obj.alphabetical[i - 1] in turing_alg_obj.table_rules:
                    turing_alg_obj.table_rules[turing_alg_obj.alphabetical[i - 1]].append(cell)
                else:
                    turing_alg_obj.table_rules[turing_alg_obj.alphabetical[i - 1]] = []
                    turing_alg_obj.table_rules[turing_alg_obj.alphabetical[i - 1]].append(cell)
            cell.grid(row=i, column=j)


def fill_rules_table(turing_alg_obj, rules_table):
    for i in range(0, len(turing_alg_obj.alphabetical)):
        current_symbol = turing_alg_obj.list_entry_alphabet[i].get()

        current_rules = rules_table.get(current_symbol)

        for index, cell in enumerate(turing_alg_obj.table_rules[current_symbol]):
            cell.insert("end", current_rules[index])


def fake_step(turing_alg_obj, turing_alg_wid):
    current_rule = turing_alg_obj.get_current_rule()

    if current_rule == "":
        messagebox.showerror(title="Ошибка",
                             message=f"Нет команды в ячейке ({turing_alg_obj.pointer_value}, Q{turing_alg_obj.index_states})",
                             parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.index_states = 0
        return True

    if ">" in current_rule:
        sym = ">"
        s = "передвигаем вправо"
    elif "<" in current_rule:
        sym = "<"
        s = "передвигаем влево"
    elif "." in current_rule:
        sym = "."
        s = "не передвигаем"
    else:
        messagebox.showerror(title="Ошибка",
                             message=f"Нет направления перехода в ячейке ({turing_alg_obj.pointer_value}, Q{turing_alg_obj.index_states})",
                             parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.index_states = 0
        return True

    ind = current_rule.index(sym)
    turing_alg_obj.index_states = int(current_rule[ind + 1:])  # состояние, в которое нужно перейти
    elem_replace = current_rule[:ind]  # элемент, на который нужно заменить

    if turing_alg_obj.index_states > turing_alg_obj.counter_states:
        messagebox.showerror(title="Ошибка", message=f"Состояния Q{turing_alg_obj.index_states} не существует",
                             parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.index_states = 0
        return True

    turing_alg_wid.list_lbl_comments[0][
        "text"] = f"1. Заменяем {turing_alg_obj.pointer_index}-й элемент на {elem_replace}"
    turing_alg_wid.list_lbl_comments[1]["text"] = f"""2. Указатель на бесконечной
ленте {s}"""
    turing_alg_wid.list_lbl_comments[2]["text"] = f"3. Переходим в состояние Q{turing_alg_obj.index_states}"

    return False


def step_alg(turing_alg_obj, turing_alg_wid):
    current_rule = turing_alg_obj.get_current_rule()

    if current_rule == "":
        messagebox.showerror(title="Ошибка",
                             message=f"Нет команды в ячейке ({turing_alg_obj.pointer_value}, Q{turing_alg_obj.index_states})",
                             parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.index_states = 0
        return True

    if ">" in current_rule:
        sym = ">"
        s = "передвигаем вправо"
    elif "<" in current_rule:
        sym = "<"
        s = "передвигаем влево"
    elif "." in current_rule:
        sym = "."
        s = "не передвигаем"
    else:
        messagebox.showerror(title="Ошибка",
                             message=f"Нет направления перехода в ячейке ({turing_alg_obj.pointer_value}, Q{turing_alg_obj.index_states})",
                             parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.index_states = 0
        return True

    ind = current_rule.index(sym)
    turing_alg_obj.index_states = int(current_rule[ind + 1:])  # состояние, в которое нужно перейти
    elem_replace = current_rule[:ind]  # элемент, на который нужно заменить

    if turing_alg_obj.index_states > turing_alg_obj.counter_states:
        messagebox.showerror(title="Ошибка", message=f"Состояния Q{turing_alg_obj.index_states} не существует",
                             parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.index_states = 0
        return True

    if elem_replace == "":
        elem_replace = " "

    turing_alg_obj.set_val_for_cur_elem(elem_replace, turing_alg_wid)

    turing_alg_obj.move_pointer(sym, turing_alg_obj, turing_alg_wid)

    turing_alg_wid.list_lbl_comments[0][
        "text"] = f"1. Заменяем {turing_alg_obj.pointer_index}-ый элемент на {elem_replace}"
    turing_alg_wid.list_lbl_comments[1]["text"] = f"""2. Указатель на бесконечной
ленте 
{s}"""
    turing_alg_wid.list_lbl_comments[2]["text"] = f"3. Переходим в состояние Q{turing_alg_obj.index_states}"

    if turing_alg_obj.index_states != 0:
        turing_alg_obj.color_current_rule()

    return False


def step_process_turing_alg(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.button_run["state"] = "disabled"

    max_ind, min_ind = max(turing_alg_wid.infinity_tape.keys()), min(turing_alg_wid.infinity_tape.keys())

    expression = {}

    for i in range(min_ind, max_ind):
        expression[i] = str(turing_alg_wid.infinity_tape[i].selected_value.get())

    turing_alg_obj.set_expression(expression)

    if turing_alg_obj.index_states != 0:
        if turing_alg_obj.counter_step == -1:
            turing_alg_obj.color_current_rule()
            turing_alg_obj.completed_error = fake_step(turing_alg_obj, turing_alg_wid)
        else:
            turing_alg_obj.completed_error = step_alg(turing_alg_obj, turing_alg_wid)

        turing_alg_obj.counter_step += 1

    if turing_alg_obj.index_states == 0:

        turing_alg_wid.button_run["state"] = "normal"

        turing_alg_obj.index_states = 1
        turing_alg_obj.counter_step = -1
        turing_alg_obj.stop_process = False

        for key in turing_alg_obj.table_rules:
            for cell in turing_alg_obj.table_rules[key]:
                cell["background"] = 'white'

        turing_alg_wid.list_lbl_comments[0]["text"] = ""
        turing_alg_wid.list_lbl_comments[1]["text"] = ""
        turing_alg_wid.list_lbl_comments[2]["text"] = ""
        if turing_alg_obj.completed_error == False and turing_alg_obj.stop_process == False:
            messagebox.showinfo(title="Информация", message="Выполнение программы завершено",
                                parent=turing_alg_wid.frame_table_rules)
        turing_alg_obj.completed_error = False
        turing_alg_obj.stop_process = False


def stop_process(turing_alg_obj, turing_alg_wid):
    messagebox.showinfo(title="Информация", message="Программа остановлена пользователем",
                        parent=turing_alg_wid.frame_table_rules)
    turing_alg_obj.index_states = 1
    turing_alg_obj.stop_process = True
    for key in turing_alg_obj.table_rules:
        for cell in turing_alg_obj.table_rules[key]:
            cell["background"] = 'white'
    print(turing_alg_obj.stop_process)

    turing_alg_wid.button_run["state"] = "normal"
    turing_alg_wid.button_step["state"] = "normal"


def process_turing_alg(turing_alg_obj, turing_alg_wid):
    turing_alg_obj.stop_process = False
    save_start_expression(turing_alg_obj, turing_alg_wid)

    turing_alg_wid.button_run["state"] = "disabled"
    turing_alg_wid.button_step["state"] = "disabled"

    while turing_alg_obj.index_states != 0:

        if turing_alg_obj.counter_step >= 1000:
            messagebox.showwarning(title="Предупреждение",
                                   message="В вашем алгоритме обнаружено больше 1000 шагов. Возможно в нем присутствует цикл. Пожалуйста, исправьте ваши правила.",
                                   parent=turing_alg_wid.frame_table_rules)
            start_tape_recovery(turing_alg_obj, turing_alg_wid)
            turing_alg_obj.completed_error = True
            break

        if turing_alg_obj.stop_process:
            messagebox.showinfo(title="Информация", message="Программа остановлена пользователем",
                                parent=turing_alg_wid.frame_table_rules)
            turing_alg_obj.completed_error = True
            break

        max_ind, min_ind = max(turing_alg_wid.infinity_tape.keys()), min(turing_alg_wid.infinity_tape.keys())

        table_of_rules, expression = turing_alg_obj.table_rules, {}

        for i in range(min_ind, max_ind):
            expression[i] = str(turing_alg_wid.infinity_tape[i].selected_value.get())

        turing_alg_obj.set_expression(expression)

        turing_alg_obj.completed_error = step_alg(turing_alg_obj, turing_alg_wid)
        turing_alg_obj.counter_step += 1

    if not turing_alg_obj.completed_error:
        messagebox.showinfo(title="Информация", message="Выполнение программы завершено",
                            parent=turing_alg_wid.frame_table_rules)
    turing_alg_obj.index_states = 1
    turing_alg_obj.counter_step = -1
    turing_alg_wid.button_run["state"] = "normal"
    turing_alg_wid.button_step["state"] = "normal"

    for key in turing_alg_obj.table_rules:
        for cell in turing_alg_obj.table_rules[key]:
            cell["background"] = 'white'

    turing_alg_wid.list_lbl_comments[0]["text"] = ""
    turing_alg_wid.list_lbl_comments[1]["text"] = ""
    turing_alg_wid.list_lbl_comments[2]["text"] = ""

    turing_alg_obj.completed_error = False


def add_column_for_states(turing_alg_obj, turing_alg_wid):
    turing_alg_obj.counter_states += 1
    cell = Tk.Entry(master=turing_alg_wid.frame_table_rules, width=5, font=('Arial', 16, 'bold'), relief="raised")
    cell.insert("end", f"Q{turing_alg_obj.counter_states}")
    cell["state"] = "disabled"
    turing_alg_obj.list_entry_states.append(cell)
    cell.grid(row=0, column=turing_alg_obj.counter_states)
    i = 1
    for keys in turing_alg_obj.table_rules:
        cell = Tk.Entry(master=turing_alg_wid.frame_table_rules, width=5, font=('Arial', 16, 'bold'), relief="raised")
        turing_alg_obj.table_rules[keys].append(cell)
        cell.grid(row=i, column=turing_alg_obj.counter_states)
        i += 1


def delete_column_for_state(turing_alg_obj, turing_alg_wid):
    if turing_alg_obj.counter_states <= 1:
        return

    cell = turing_alg_obj.list_entry_states[turing_alg_obj.counter_states]
    cell.destroy()
    turing_alg_obj.list_entry_states.pop()
    for key in turing_alg_obj.table_rules:
        cell = turing_alg_obj.table_rules[key][turing_alg_obj.counter_states - 1]
        cell.destroy()
        turing_alg_obj.table_rules[key].pop()
    turing_alg_obj.counter_states -= 1


def help_trainer(dict_windows):
    window = Tk.Toplevel()
    window.title("Как работать с тренажером?")
    window_width_center = (window.winfo_screenwidth()) // 2 - 350
    window_height_center = (window.winfo_screenheight()) // 2 - 300
    window.geometry("700x600+{}+{}".format(window_width_center, window_height_center))
    window.config(background="white")
    window.resizable(width=False, height=False)

    label = Tk.Label(window, text="Как работать с тренажером?", justify="center", font=("Gabriola", "20"),
                     background="white")
    label.place(x=150, y=5)

    text = Tk.Frame(master=window, width=675, height=540, background="white")
    text.place(x=10, y=50)

    label_info = Tk.Label(master=text, text=TRAINER, justify="left", font=("Bahnschrift Light", "12"),
                          background="white")
    label_info.place(x=5, y=5)


def first_task_laboratory_work(turing_alg_obj, turing_alg_wid):

    turing_alg_wid.text_task_condition.delete("1.0", "end")
    if turing_alg_wid.tests:
        turing_alg_wid.tests.destroy()

    #генерация условия задания 1
    basis = random.randint(3, 5)
    free_member = random.randint(0, basis-1)
    text_task = f'Составьте программу для машины Тьюринга, которая приписывает букву «И» в начале строки из палочек, ' \
                f'если количество палочек в строке представимо в виде {basis}k+{free_member} и букву «Л», если нет'
    turing_alg_wid.text_task_condition.insert("end", text_task)

    #генерация тестов
    table_tests = []
    test_one = random.randint(1, 7)*2
    if (test_one - free_member) % basis == 0:
        test_one_answer = 'И'+'|'*test_one
    else:
        test_one_answer = 'Л'+'|'*test_one
    table_tests.append(tuple([test_one, test_one_answer]))
    test_two = random.randint(1, 7)*2+1
    if (test_two - free_member) % basis == 0:
        test_two_answer = 'И'+'|'*test_two
    else:
        test_two_answer = 'Л'+'|'*test_two
    table_tests.append(tuple([test_two, test_two_answer]))

    test = Tk.Frame(master=turing_alg_wid.text_task_condition, background="white", border=10)
    test.place(x=10, y=40)
    turing_alg_wid.tests = test

    columns = ("input", "output")
    tree = ttk.Treeview(master=test, columns=columns, show="headings")
    tree.pack(fill="both", expand=1)
    tree.heading("input", text="input")
    tree.heading("output", text="output")

    for test in table_tests:
        tree.insert("", "end", values=test)


def convert_to_base(n, base):
    digits = []
    while n > 0:
        digits.append(n % base)
        n = n // base
    digits.reverse()
    return digits


def second_task_laboratory_work(turing_alg_obj, turing_alg_wid):

    turing_alg_wid.text_task_condition.delete("1.0", "end")
    if turing_alg_wid.tests:
        turing_alg_wid.tests.destroy()

    # генерация условия задания 2
    basis = random.randint(3, 5)
    increase_by_number = random.randint(2, basis - 1)
    text_task = f'Составьте программу для машины Тьюринга, которая умножает натуральное число, записанное на ленте в ' \
                f'{basis}-ичной системе счисления на {increase_by_number}'
    turing_alg_wid.text_task_condition.insert("end", text_task)

    #генерация тестов
    table_tests = []
    test_one = random.randint(10000, 50000)
    input_test_one = convert_to_base(test_one, basis) #число в заданной системе счисления
    result_decimal = convert_to_base(test_one*increase_by_number, basis) #результат умножения в заданной системе счисления

    table_tests.append(tuple([input_test_one, result_decimal]))

    test = Tk.Frame(master=turing_alg_wid.text_task_condition, background="white", border=10)
    test.place(x=10, y=40)
    turing_alg_wid.tests = test

    columns = ("input", "output")
    tree = ttk.Treeview(master=test, columns=columns, show="headings")
    tree.pack(fill="both", expand=1)
    tree.heading("input", text="input")
    tree.heading("output", text="output")

    for test in table_tests:
        tree.insert("", "end", values=test)


def third_task_laboratory_work(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.text_task_condition.delete("1.0", "end")
    if turing_alg_wid.tests:
        turing_alg_wid.tests.destroy()

    # генерация условия задания 3
    divider = random.randint(3, 7)
    text_task = f'Составьте программу для машины Тьюринга, которая вычисляет функцию [a/{divider}],  ' \
                f'где [ ] означает целую часть, а число представлено на ленте в виде группы палочек'
    turing_alg_wid.text_task_condition.insert("end", text_task)

    # генерация тестов
    table_tests = []

    test_one = divider*random.randint(1, 3)
    test_one_answer = test_one // divider
    table_tests.append(tuple([test_one, test_one_answer]))
    test_two = divider + random.randint(1, 3)*divider - random.randint(1, divider-1)
    test_two_answer = test_two // divider
    table_tests.append(tuple([test_two, test_two_answer]))

    test = Tk.Frame(master=turing_alg_wid.text_task_condition, background="white", border=10)
    test.place(x=10, y=40)
    turing_alg_wid.tests = test

    columns = ("input", "output")
    tree = ttk.Treeview(master=test, columns=columns, show="headings")
    tree.pack(fill="both", expand=1)
    tree.heading("input", text="input")
    tree.heading("output", text="output")

    for test in table_tests:
        tree.insert("", "end", values=test)


def fourth_task_laboratory_work(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.text_task_condition.delete("1.0", "end")
    if turing_alg_wid.tests:
        turing_alg_wid.tests.destroy()

    # генерация условия задания 4
    basis = random.randint(3, 5)
    increase_by_number = str(random.randint(2, basis - 1)) #какие цифры ищем
    side = random.choice(['справа','слева'])
    text_task = f'Составьте программу для машины Тьюринга, которая приписывает {side} к числу в ' \
                f'{basis}-ичной системе счисления записанному на ленте столько палочек, сколько в нем цифр «{increase_by_number}»'
    turing_alg_wid.text_task_condition.insert("end", text_task)

    # генерация тестов
    table_tests = []
    test_one = convert_to_base(random.randint(100, 500), basis)
    print(type(test_one))
    print(test_one)
    count_one = test_one.count(int(increase_by_number))
    print(count_one)

    if count_one > 0:
        if side == 'справа':
            test_one_answer = test_one.copy()
            test_one_answer.append('|'*count_one)
        else:
            test_one_answer = ['|'*count_one] + test_one
    else:
        test_one_answer = test_one.copy()

    table_tests.append(tuple([test_one, test_one_answer]))

    flag = True

    test_two = None

    while flag:
        test_two = convert_to_base(random.randint(100, 500), basis)

        if int(increase_by_number) not in test_two:
            flag = False

    table_tests.append(tuple([test_two, test_two]))

    test = Tk.Frame(master=turing_alg_wid.text_task_condition, background="white", border=10)
    test.place(x=10, y=40)
    turing_alg_wid.tests = test

    columns = ("input", "output")
    tree = ttk.Treeview(master=test, columns=columns, show="headings")
    tree.pack(fill="both", expand=1)
    tree.heading("input", text="input")
    tree.heading("output", text="output")

    for test in table_tests:
        tree.insert("", "end", values=test)


def simulator_turing_machine(dict_windows):
    window_machine_turing = dict_windows.get("window_machine_turing")

    frame_title = Tk.Frame(master=window_machine_turing, width=1200, height=300, background=rgb_hack((1, 116, 64)))
    frame_title.place(x=0, y=45)

    label_task_сondition = Tk.Label(master=window_machine_turing, text="Условие задачи: ", height=1, justify="left",
                                    font=("Gabriola", "20"), background=rgb_hack((1, 116, 64)))
    label_task_сondition.place(x=10, y=45)

    label_alphabetical = Tk.Label(master=window_machine_turing, text="Алфавит: ", height=1, justify="left",
                                  font=("Gabriola", "20"), background=rgb_hack((1, 116, 64)))
    label_alphabetical.place(x=10, y=215)
    entry_alphabetical = Tk.Entry(master=window_machine_turing, width=77, font=("Arial", "16", "italic"))
    entry_alphabetical.place(x=110, y=230)
    button_alphabetical = Tk.Button(master=window_machine_turing, text="Ввод алфавита", width=15, height=1,
                                    font=("Arial", "12", "italic"), cursor="hand2",
                                    command=lambda: input_alphabet(turing_alg_obj, entry_alphabetical.get(),
                                                                   turing_alg_wid))
    button_alphabetical.place(x=1050, y=230)

    text_task_condition = Tk.Text(master=window_machine_turing, width=147, height=8)
    text_task_condition.place(x=10, y=85)

    container = ttk.Frame(master=window_machine_turing, width=800, height=250)
    canvas = Tk.Canvas(master=container, width=800, height=250, background="white", border=0)
    scrollbary = ttk.Scrollbar(master=container, orient=Tk.VERTICAL, command=canvas.yview)
    scrollbarx = ttk.Scrollbar(master=container, orient=Tk.HORIZONTAL, command=canvas.xview)

    frame_table_rules = Tk.Frame(master=canvas, width=800, height=250, border=10, background=rgb_hack((1, 116, 64)))
    frame_table_rules.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=frame_table_rules, anchor="nw")
    canvas.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    container.place(x=10, y=430, width=850, height=250)
    canvas.pack(side="left", expand=True)

    scrollbarx.pack(side="bottom", fill=Tk.X)
    scrollbary.pack(side="right", fill=Tk.Y)

    frame_comments = Tk.Frame(master=window_machine_turing, width=305, height=310, background=rgb_hack((1, 116, 64)),
                              border=10)
    frame_comments.place(x=875, y=430)
    label_com = Tk.Label(master=window_machine_turing, text="Комментарии", height=1, justify="left",
                         font=("Gabriola", "20"), background="white")
    label_com.place(x=960, y=370)

    frame_infinity_tape = Tk.Frame(master=window_machine_turing, width=1140, height=100)
    frame_infinity_tape.place(x=30, y=275)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_machine_turing)
    label_point = Tk.Label(window_machine_turing, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=41)
    label_point.place(x=547, y=0)

    # place_y = 0
    list_lbl_comments = []

    for i in range(3):
        lbl = Tk.Label(master=frame_comments, justify="left", font=("Arial", "14", "italic"),
                       background=rgb_hack((1, 116, 64)), border=0)
        list_lbl_comments.append(lbl)

    list_lbl_comments[0].place(x=0, y=5)
    list_lbl_comments[1].place(x=0, y=45)
    list_lbl_comments[2].place(x=0, y=115)

    alphabetical = ["0", "1", " "]

    infinity_tape = {}
    output_elm_ids = [-9, 9]

    counter_states = 2  # начальное число состояний

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_machine_turing)
    label_right = Tk.Label(window_machine_turing, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_machine_turing, image=photo_right, width=1, height=6,
                             command=lambda: movement_right(turing_alg_obj, turing_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_machine_turing)
    label_left = Tk.Label(window_machine_turing, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_machine_turing, image=photo_left, width=1, height=6,
                            command=lambda: movement_left(turing_alg_obj, turing_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)

    img_run = Image.open(Path.cwd() / "Image" / "Play.png")
    photo_run = ImageTk.PhotoImage(img_run, master=window_machine_turing)
    label_run = Tk.Label(window_machine_turing, image=photo_run)
    label_run.image = photo_run
    button_run = Tk.Button(master=window_machine_turing, text="Старт  ", image=photo_run, compound="right", width=100,
                           height=20, cursor="hand2", font=("Gabriola", "20"), state="normal",
                           command=lambda: process_turing_alg(turing_alg_obj, turing_alg_wid))
    button_run.place(x=10, y=10)

    img_step = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_step = ImageTk.PhotoImage(img_step, master=window_machine_turing)
    label_step = Tk.Label(window_machine_turing, image=photo_step)
    label_step.image = photo_step
    button_step = Tk.Button(master=window_machine_turing, text="Шаг  ", image=photo_step, compound="right", width=100,
                            height=20, cursor="hand2", font=("Gabriola", "20"), state="normal",
                            command=lambda: step_process_turing_alg(turing_alg_obj, turing_alg_wid))
    button_step.place(x=130, y=10)

    img_stop = Image.open(Path.cwd() / "Image" / "Stop.png")
    photo_stop = ImageTk.PhotoImage(img_stop, master=window_machine_turing)
    label_stop = Tk.Label(window_machine_turing, image=photo_stop)
    label_stop.image = photo_stop
    button_stop = Tk.Button(master=window_machine_turing, text="Остановить  ", image=photo_stop, compound="right",
                            width=150, height=20, cursor="hand2", font=("Gabriola", "20"),
                            command=lambda: stop_process(turing_alg_obj, turing_alg_wid))
    button_stop.place(x=250, y=10)

    img_add = Image.open(Path.cwd() / "Image" / "add.png")
    photo_add = ImageTk.PhotoImage(img_add, master=window_machine_turing)
    label_add = Tk.Label(window_machine_turing, image=photo_add)
    label_add.image = photo_add
    button_add_column = Tk.Button(master=window_machine_turing, image=photo_add, width=40, height=40,
                                  background="white", relief="flat", cursor="hand2", state="normal",
                                  command=lambda: add_column_for_states(turing_alg_obj, turing_alg_wid))
    button_add_column.place(x=10, y=380)

    img_del = Image.open(Path.cwd() / "Image" / "del.png")
    photo_del = ImageTk.PhotoImage(img_del, master=window_machine_turing)
    label_del = Tk.Label(window_machine_turing, image=photo_del)
    label_del.image = photo_del
    button_delete_column = Tk.Button(master=window_machine_turing, image=photo_del, width=40, height=40,
                                     background="white", relief="flat", cursor="hand2", state="normal",
                                     command=lambda: delete_column_for_state(turing_alg_obj, turing_alg_wid))
    button_delete_column.place(x=60, y=380)

    turing_alg_obj = TuringAlg(0, alphabetical, 1, counter_states)
    turing_alg_wid = ObjTuringAlg(infinity_tape, frame_infinity_tape, frame_table_rules, output_elm_ids,
                                  text_task_condition, button_right, button_left, list_lbl_comments, entry_alphabetical,
                                  button_run, button_step)

    creating_rules_table(turing_alg_obj, turing_alg_wid)
    creating_infinity_tape(turing_alg_obj, turing_alg_wid)
    save_expression(turing_alg_obj, turing_alg_wid)

    # создание верхнего меню
    mainmenu = Tk.Menu(master=window_machine_turing)

    filemenu = Tk.Menu(master=mainmenu, tearoff=0)
    filemenu.add_command(label="Новый", command=lambda: creating_new_file(turing_alg_obj, turing_alg_wid))
    filemenu.add_command(label="Открыть...", command=lambda: read_example(turing_alg_obj, turing_alg_wid, dict_windows))
    filemenu.add_command(label="Сохранить как ...",
                         command=lambda: save_file(turing_alg_obj, turing_alg_wid, dict_windows))
    filemenu.add_separator()
    filemenu.add_command(label="Выход", command=lambda: return_window_for_algorithms(dict_windows))

    tapemenu = Tk.Menu(master=mainmenu, tearoff=0)
    tapemenu.add_command(label="Сохранить ленту", command=lambda: save_expression(turing_alg_obj, turing_alg_wid))
    tapemenu.add_command(label="Восстановить ленту", command=lambda: tape_recovery(turing_alg_obj, turing_alg_wid))

    labworkmenu = Tk.Menu(master=mainmenu, tearoff=0)
    labworkmenu.add_command(label="Задание 1", command=lambda: first_task_laboratory_work(turing_alg_obj, turing_alg_wid))
    labworkmenu.add_command(label="Задание 2", command=lambda: second_task_laboratory_work(turing_alg_obj, turing_alg_wid))
    labworkmenu.add_command(label="Задание 3", command=lambda: third_task_laboratory_work(turing_alg_obj, turing_alg_wid))
    labworkmenu.add_command(label="Задание 4", command=lambda: fourth_task_laboratory_work(turing_alg_obj, turing_alg_wid))
    labworkmenu.add_command(label="Задание 5")

    processmenu = Tk.Menu(master=mainmenu, tearoff=0)
    processmenu.add_command(label="Запуск", command=lambda: process_turing_alg(turing_alg_obj, turing_alg_wid))
    processmenu.add_command(label="Выполнить шаг",
                            command=lambda: step_process_turing_alg(turing_alg_obj, turing_alg_wid))

    helpmenu = Tk.Menu(master=mainmenu, tearoff=0)
    helpmenu.add_command(label="Как работать с тренажером", command=lambda: help_trainer(dict_windows))

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Лента", menu=tapemenu)
    mainmenu.add_cascade(label="Лабораторная работа", menu=labworkmenu)
    mainmenu.add_cascade(label="Выполнение", menu=processmenu)
    mainmenu.add_cascade(label="?", menu=helpmenu)

    window_machine_turing.config(menu=mainmenu)

    window_machine_turing.protocol("WM_DELETE_WINDOW", lambda: return_window_for_algorithms(dict_windows))
