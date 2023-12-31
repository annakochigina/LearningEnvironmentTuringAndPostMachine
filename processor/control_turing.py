import tkinter
import tkinter as Tk
from tkinter import messagebox
from random import randint
from tkinter import ttk
import re
import const.text as text
import tkinter.filedialog as fd
import json
from classes.TuringAlg import TuringAlg
from classes.ObjTuringAlg import ObjTuringAlg
from classes.MyOptionMenu import MyOptionMenu
from PIL import Image, ImageTk
from pathlib import Path

CONTROL_TURING = text.CONST_CONTROL_START


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def return_window_for_algorithms(dict_windows):
    if messagebox.askokcancel("Завершение контроля", "Вы уверены, что хотите завершить контроль?",
                              parent=dict_windows["window_control_turing"]):
        dict_windows["window_control_turing"].destroy()
        dict_windows["window_for_algorithms"].deiconify()


def destroy_widgets(widgets):
    for obj in widgets:
        obj.destroy()
    return []


def delete_option_menu_from_frame(frame: Tk.Frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tkinter.OptionMenu):
            widget.place(x=-1000, y=-1000)


def create_control_turing(dict_windows):
    window_control_turing = Tk.Tk()
    window_control_turing_width_center = (window_control_turing.winfo_screenwidth()) // 2 - 600
    window_control_turing_height_center = (window_control_turing.winfo_screenheight()) // 2 - 375
    window_control_turing.geometry(
        "1200x750+{}+{}".format(window_control_turing_width_center, window_control_turing_height_center))
    window_control_turing.resizable(width=False, height=False)
    window_control_turing.config(bg="white")
    dict_windows["window_control_turing"] = window_control_turing
    window_control_turing.title("Контроль - машина Тьюринга")

    start_control_turing(dict_windows)


def start_control_turing(dict_windows):
    widgets = []
    window_control_turing = dict_windows["window_control_turing"]

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, relief="flat",
                            background="white", cursor="hand2",
                            command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    img_con = Image.open(Path.cwd() / "Image" / "controltime.png")
    photo_con = ImageTk.PhotoImage(img_con, master=window_control_turing)
    label_con = Tk.Label(window_control_turing, image=photo_con)
    label_con.image = photo_con
    label_control = Tk.Label(master=window_control_turing, image=photo_con, width=100, height=100, justify="center",
                             background="white", font=("Gabriola", "40", "bold"))
    label_control.place(x=0, y=0)
    widgets.append(label_control)

    label_start = Tk.Label(master=window_control_turing, text="Контроль", justify="center", width=35,
                           background=rgb_hack((1, 116, 64)), font=("Gabriola", "40"))
    label_start.place(x=200, y=200)
    widgets.append(label_start)

    frame_description_control = Tk.Frame(master=window_control_turing, width=775, height=400,
                                         background=rgb_hack((1, 116, 64)), border=15)
    frame_description_control.place(x=200, y=350)
    widgets.append(frame_description_control)

    label_description_control = Tk.Label(master=frame_description_control, width=65, height=7, text=CONTROL_TURING,
                                         justify="center", font=("Gabriola", "20"), background="white")
    label_description_control.place(x=10, y=10)
    widgets.append(label_description_control)

    img_start = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_start = ImageTk.PhotoImage(img_start, master=window_control_turing)
    label_start = Tk.Label(window_control_turing, image=photo_start)
    label_start.image = photo_start
    button_start = Tk.Button(master=window_control_turing, text="Начать контроль  ", image=photo_start,
                             compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                             relief="flat", cursor="hand2", command=lambda: first_task_turing(dict_windows, widgets))
    button_start.place(x=980, y=705)
    widgets.append(button_start)

    window_control_turing.protocol("WM_DELETE_WINDOW", lambda: return_window_for_algorithms(dict_windows))


def return_window_start_control(dict_windows, widgets, turing_alg_obj, turing_alg_wid, test_completed=False):
    print(test_completed)
    if not test_completed and messagebox.askokcancel("Завершение контроля",
                                                     "Ваши результаты будут сброшены. Вы уверены, что хотите выйти?",
                                                     parent=turing_alg_wid.frame_table_rules):
        destroy_widgets(widgets)

        turing_alg_wid.frame_infinity_tape.destroy()
        turing_alg_wid.frame_table_rules.destroy()
        turing_alg_wid.text_task_condition.destroy()
        turing_alg_wid.button_right.destroy()
        turing_alg_wid.button_left.destroy()

        start_control_turing(dict_windows)

    elif test_completed:
        print(test_completed)
        destroy_widgets(widgets)

        turing_alg_wid.frame_infinity_tape.destroy()
        turing_alg_wid.frame_table_rules.destroy()
        turing_alg_wid.text_task_condition.destroy()
        turing_alg_wid.button_right.destroy()
        turing_alg_wid.button_left.destroy()

        start_control_turing(dict_windows)


def read_and_create_task(turing_alg_obj, turing_alg_wid, number_task, entry_answer_stud=None):
    with open("TASKS_TURING.json", encoding='utf-8') as f:
        example_info = json.load(f)

    list_tasks = []
    for dct in example_info:
        if dct["type"] == number_task:
            list_tasks.append(dct)

    number_option = randint(0, 4)
    current_tasks = list_tasks[number_option]

    alphabetical_text = current_tasks.get("alphabetical")
    counter_states = current_tasks.get("counter_states")
    pointer_index = current_tasks.get("pointer_index")
    table_rules = current_tasks.get("table_rules")
    expression_info = current_tasks.get("expression")
    task_condition = current_tasks.get("task_condition")

    turing_alg_obj.pointer_index = pointer_index
    turing_alg_obj.counter_states = counter_states
    turing_alg_obj.alphabetical = list(alphabetical_text)
    turing_alg_obj.alphabetical.append(" ")
    turing_alg_wid.text_task_condition.insert("end", task_condition)

    creating_rules_table(turing_alg_obj, turing_alg_wid)

    fill_rules_table(turing_alg_obj, table_rules)
    create_and_fill_infinity_tape(turing_alg_obj, turing_alg_wid, expression_info, pointer_index)

    for key in turing_alg_obj.table_rules:
        for elem in turing_alg_obj.table_rules[key]:
            elem["state"] = "disabled"

    if number_task == 3:
        num_row = current_tasks.get("num_cell_row")
        num_col = current_tasks.get("num_cell_col")
        cell = turing_alg_obj.table_rules[num_row][num_col]
        cell["state"] = "normal"
        turing_alg_wid.entry_answer_stud_third = cell

    if number_task == 4:
        turing_alg_wid.lst_var = current_tasks.get("var")

    turing_alg_wid.list_true_answer.append(current_tasks.get("answer"))


def creating_infinity_tape(turing_alg_obj, turing_alg_wid):
    place_x = 0
    turing_alg_obj.pointer_index = 0

    for ind in range(-9, 10):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        current_opt_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        # current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        # current_opt_menu.place(x=place_x, y=60, width=60, height=40)
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, turing_alg_obj.alphabetical)
        turing_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=turing_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"))
        lbl.place(x=place_x + 20, y=44)
        turing_alg_wid.list_label_ind.append(lbl)

        place_x += 60


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
    for i in range(len(turing_alg_obj.alphabetical) + 1):  # создание таблицы правил
        for j in range(turing_alg_obj.counter_states + 1):
            cell = Tk.Entry(master=turing_alg_wid.frame_table_rules, width=5, font=('Arial', 16, 'bold', "italic"),
                            relief="raised")
            if j == 0 and i > 0:
                cell.insert("end", turing_alg_obj.alphabetical[i - 1])
                cell["state"] = "disabled"
                turing_alg_obj.list_entry_alphabet.append(cell)
            elif i == 0 and j > 0:
                cell.insert("end", f"Q{j}")
                cell["state"] = "disabled"
                turing_alg_obj.list_entry_states.append(cell)
            elif i == 0 and j == 0:
                turing_alg_obj.list_entry_states.append(cell)
                cell["state"] = "disabled"
            if i > 0 and j > 0:
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


def create_and_fill_infinity_tape(turing_alg_obj, turing_alg_wid, expression_info, pointer_index):
    place_x = 0

    turing_alg_obj.pointer_index = pointer_index

    min_ind, max_ind = min(expression_info.keys()), max(expression_info.keys())
    min_ind, max_ind = min([int(min_ind), pointer_index - 9]), max([int(max_ind), pointer_index + 10])

    turing_alg_wid.output_elm_ids = [pointer_index - 9, pointer_index + 10]

    for ind in range(min_ind, max_ind + 1):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(expression_info.get(str(ind), " "))

        current_opt_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, turing_alg_obj.alphabetical)
        turing_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=turing_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"), background="white")

        if turing_alg_wid.output_elm_ids[0] <= ind < turing_alg_wid.output_elm_ids[1]:
            current_opt_menu.place(x=place_x, y=63, width=60, height=40)
            lbl.place(x=place_x + 20, y=40)
            place_x += 60

        turing_alg_wid.list_label_ind.append(lbl)


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


def cleaning_widgets(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.text_task_condition.delete("1.0", "end")

    turing_alg_wid.output_elm_ids = [-9, 9]

    delete_rules_table(turing_alg_obj)

    for elem in turing_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    turing_alg_wid.list_label_ind.clear()

    delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
    turing_alg_wid.infinity_tape.clear()


def first_task_turing(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]
    #
    # frame_fon = Tk.Frame(master=window_control_turing, width=1200, height=375, background=rgb_hack((1, 116, 64)))
    # frame_fon.place(x=0, y=0)

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 1", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=10, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", relief="flat",
                            command=lambda: return_window_start_control(dict_windows, widgets, turing_alg_obj,
                                                                        turing_alg_wid))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    text_task_condition = Tk.Text(master=window_control_turing, width=131, height=8, font=("Times New Roman", "14"))
    text_task_condition.place(x=10, y=90)

    frame_table_rules = Tk.Frame(master=window_control_turing, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=50, y=430)
    # width = 850, height = 250

    frame_infinity_tape = Tk.Frame(master=window_control_turing, width=1140, height=100, background="white")
    frame_infinity_tape.place(x=30, y=275)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_control_turing)
    label_point = Tk.Label(window_control_turing, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40, background="white")
    label_point.place(x=547, y=0)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    frame_answer = Tk.Frame(master=window_control_turing, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer_stud = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer_stud.place(x=1, y=1)
    widgets.append(entry_answer_stud)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: second_task_turing(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                               entry_answer_stud))
    button_next.place(x=960, y=705)
    widgets.append(button_next)

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_control_turing)
    label_right = Tk.Label(window_control_turing, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_control_turing, image=photo_right, width=1, height=6,
                             command=lambda: movement_right(turing_alg_obj, turing_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_control_turing)
    label_left = Tk.Label(window_control_turing, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_control_turing, image=photo_left, width=1, height=6,
                            command=lambda: movement_left(turing_alg_obj, turing_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)

    alphabetical = []
    infinity_tape = {}
    counter_states = 2
    output_elm_ids = [-9, 9]
    turing_alg_obj = TuringAlg(0, alphabetical, 1, counter_states)
    turing_alg_wid = ObjTuringAlg(infinity_tape, frame_infinity_tape, frame_table_rules, output_elm_ids,
                                  text_task_condition, button_right, button_left)

    read_and_create_task(turing_alg_obj, turing_alg_wid, 1)


def second_task_turing(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud):
    turing_alg_wid.list_answer_stud.append(entry_answer_stud.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 2", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=10, y=10)
    widgets.append(label_number_task)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", relief="flat",
                            command=lambda: return_window_start_control(dict_windows, widgets, turing_alg_obj,
                                                                        turing_alg_wid))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    frame_answer = Tk.Frame(master=window_control_turing, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer_stud = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer_stud.place(x=1, y=1)
    widgets.append(entry_answer_stud)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: third_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                       entry_answer_stud))
    button_next.place(x=960, y=705)
    widgets.append(button_next)

    read_and_create_task(turing_alg_obj, turing_alg_wid, 2)


def third_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud):
    turing_alg_wid.list_answer_stud.append(entry_answer_stud.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 3", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=10, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", relief="flat",
                            command=lambda: return_window_start_control(dict_windows, widgets, turing_alg_obj,
                                                                        turing_alg_wid))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    entry_answer_stud = Tk.Entry(master=window_control_turing, width=20, font=('Arial', 16, 'bold'), relief="raised")
    widgets.append(entry_answer_stud)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: fourth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                        entry_answer_stud))
    button_next.place(x=960, y=705)
    widgets.append(button_next)

    read_and_create_task(turing_alg_obj, turing_alg_wid, 3, entry_answer_stud)


def fourth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud):
    turing_alg_wid.list_answer_stud.append(turing_alg_wid.entry_answer_stud_third.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 4", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=10, y=10)
    widgets.append(label_number_task)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=700, y=425)
    widgets.append(label_answer)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", relief="flat",
                            command=lambda: return_window_start_control(dict_windows, widgets, turing_alg_obj,
                                                                        turing_alg_wid))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    read_and_create_task(turing_alg_obj, turing_alg_wid, 4)

    turing_alg_wid.var = Tk.StringVar()

    opt_one = Tk.Radiobutton(master=window_control_turing, text=turing_alg_wid.lst_var[0], height=2,
                             variable=turing_alg_wid.var, value=turing_alg_wid.lst_var[0], font=('Arial', 12),
                             background="white", command=lambda: change(turing_alg_wid, turing_alg_wid.lst_var[0]))
    widgets.append(opt_one)
    opt_two = Tk.Radiobutton(master=window_control_turing, text=turing_alg_wid.lst_var[1], height=2,
                             variable=turing_alg_wid.var, font=('Arial', 12), value=turing_alg_wid.lst_var[1],
                             background="white", command=lambda: change(turing_alg_wid, turing_alg_wid.lst_var[1]))
    widgets.append(opt_two)
    opt_three = Tk.Radiobutton(master=window_control_turing, text=turing_alg_wid.lst_var[2], height=2,
                               variable=turing_alg_wid.var, font=('Arial', 12), value=turing_alg_wid.lst_var[2],
                               background="white", command=lambda: change(turing_alg_wid, turing_alg_wid.lst_var[2]))
    widgets.append(opt_three)
    opt_four = Tk.Radiobutton(master=window_control_turing, text=turing_alg_wid.lst_var[3], height=2,
                              variable=turing_alg_wid.var, font=('Arial', 12), value=turing_alg_wid.lst_var[3],
                              background="white", command=lambda: change(turing_alg_wid, turing_alg_wid.lst_var[3]))
    widgets.append(opt_four)
    opt_one.place(x=700, y=485)
    opt_two.place(x=700, y=525)
    opt_three.place(x=700, y=564)
    opt_four.place(x=700, y=605)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: fifth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid))
    button_next.place(x=960, y=705)
    widgets.append(button_next)


def change(turing_alg_wid, val):
    turing_alg_wid.var = val


def fifth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid):
    turing_alg_wid.list_answer_stud.append(turing_alg_wid.var)

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 5", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=10, y=10)
    widgets.append(label_number_task)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    frame_answer = Tk.Frame(master=window_control_turing, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer_stud = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer_stud.place(x=1, y=1)
    widgets.append(entry_answer_stud)

    img_end = Image.open(Path.cwd() / "Image" / "end.png")
    photo_end = ImageTk.PhotoImage(img_end, master=window_control_turing)
    label_end = Tk.Label(window_control_turing, image=photo_end)
    label_end.image = photo_end
    button_end = Tk.Button(master=window_control_turing, text="Завершить тест  ", image=photo_end, compound="right",
                           font=("Gabriola", "20"), width=210, height=50, background="white", relief="flat",
                           cursor="hand2",
                           command=lambda: test_results(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                        entry_answer_stud))
    button_end.place(x=960, y=690)
    widgets.append(button_end)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", relief="flat",
                            command=lambda: return_window_start_control(dict_windows, widgets, turing_alg_obj,
                                                                        turing_alg_wid))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    read_and_create_task(turing_alg_obj, turing_alg_wid, 5)


def test_results(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud):
    turing_alg_wid.list_answer_stud.append(entry_answer_stud.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)
    turing_alg_wid.frame_infinity_tape.destroy()
    turing_alg_wid.frame_table_rules.destroy()
    turing_alg_wid.text_task_condition.destroy()
    turing_alg_wid.button_right.destroy()
    turing_alg_wid.button_left.destroy()

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    counter = 0
    for i in range(len(turing_alg_wid.list_answer_stud)):
        if turing_alg_wid.list_answer_stud[i] == turing_alg_wid.list_true_answer[i]:
            counter += 1
            if i == 4:
                counter += 1
    print(turing_alg_wid.list_answer_stud)
    print(turing_alg_wid.list_true_answer)

    label_res = Tk.Label(master=window_control_turing, text="Ваши результаты", justify="center", width=35,
                         background=rgb_hack((1, 116, 64)), font=("Gabriola", "40"))
    label_res.place(x=200, y=200)
    widgets.append(label_res)

    frame_description_control = Tk.Frame(master=window_control_turing, width=775, height=400,
                                         background=rgb_hack((1, 116, 64)), border=15)
    frame_description_control.place(x=200, y=350)
    widgets.append(frame_description_control)

    label_description_res = Tk.Label(master=frame_description_control,
                                     text=f"По результатам теста вы набрали: {counter}/6\n Вы можете пройти тест заново. Задания будут отличаться",
                                     width=65, height=7, justify="center", font=("Gabriola", "20"), background="white")
    label_description_res.place(x=10, y=10)
    widgets.append(label_description_res)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_control_turing)
    label_exit = Tk.Label(window_control_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_control_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", relief="flat",
                            command=lambda: return_window_start_control(dict_windows, widgets, turing_alg_obj,
                                                                        turing_alg_wid, True))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    img_repeat = Image.open(Path.cwd() / "Image" / "repeat.png")
    photo_repeat = ImageTk.PhotoImage(img_repeat, master=window_control_turing)
    label_repeat = Tk.Label(window_control_turing, image=photo_repeat)
    label_repeat.image = photo_repeat
    button_repeat = Tk.Button(master=window_control_turing, text="Пройти заново  ", image=photo_repeat,
                              compound="right", font=("Gabriola", "20"), width=200, height=50, background="white",
                              relief="flat", cursor="hand2", command=lambda: first_task_turing(dict_windows, widgets))
    button_repeat.place(x=980, y=690)
    widgets.append(button_repeat)
