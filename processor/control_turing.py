import tkinter
import tkinter as Tk
from tkinter import messagebox
from random import randint
# from tkinter import ttk
import re, os, random, string
import const.text as text
# import tkinter.filedialog as fd
import json
from classes.TuringAlg import TuringAlg
from classes.ObjTuringAlg import ObjTuringAlg
from classes.MyOptionMenu import MyOptionMenu
from PIL import Image, ImageTk
from pathlib import Path

CONTROL_TURING = text.CONST_CONTROL_TURING_START
FIRST_TASK = text.CONST_LEARN_FIRST_TASK
SECOND_TASK = text.CONST_LEARN_SECOND_TASK_TURING


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
    label_start.place(x=200, y=100)
    widgets.append(label_start)

    frame_description_control = Tk.Frame(master=window_control_turing, width=775, height=550,
                                         background=rgb_hack((1, 116, 64)), border=15)
    frame_description_control.place(x=200, y=250)
    widgets.append(frame_description_control)

    label_description_control = Tk.Label(master=frame_description_control, width=65, height=9, text=CONTROL_TURING,
                                         justify="center", font=("Gabriola", "20"), background="white")
    label_description_control.place(x=10, y=10)
    widgets.append(label_description_control)

    entry_surname_stud = Tk.Entry(master=label_description_control, width=30, font=('Cambria', 16, 'bold'), relief="groove", justify="center", highlightthickness=2)
    entry_surname_stud.place(x=200, y=400)
    widgets.append(entry_surname_stud)

    img_start = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_start = ImageTk.PhotoImage(img_start, master=window_control_turing)
    label_start = Tk.Label(window_control_turing, image=photo_start)
    label_start.image = photo_start
    button_start = Tk.Button(master=window_control_turing, text="Начать контроль  ", image=photo_start,
                             compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                             relief="flat", cursor="hand2", command=lambda: first_task_turing(dict_windows, widgets, entry_surname_stud))
    button_start.place(x=980, y=705)
    widgets.append(button_start)

    window_control_turing.protocol("WM_DELETE_WINDOW", lambda: return_window_for_algorithms(dict_windows))


def return_window_start_control(dict_windows, widgets, turing_alg_obj, turing_alg_wid, test_completed=False):
    if not test_completed and messagebox.askokcancel("Завершение контроля",
                                                     "Ваши результаты будут сброшены. Вы уверены, что хотите выйти?",
                                                     parent=turing_alg_wid.frame_table_rules):
        destroy_widgets(widgets)

        if turing_alg_wid.frame_infinity_tape:
            turing_alg_wid.frame_infinity_tape.destroy()
            turing_alg_wid.frame_table_rules.destroy()
        if turing_alg_wid.text_task_condition:
            turing_alg_wid.text_task_condition.destroy()
        if turing_alg_wid.button_right:
            turing_alg_wid.button_right.destroy()
            turing_alg_wid.button_left.destroy()

        start_control_turing(dict_windows)

    elif test_completed:
        destroy_widgets(widgets)

        turing_alg_wid.frame_infinity_tape.destroy()
        turing_alg_wid.frame_table_rules.destroy()
        turing_alg_wid.text_task_condition.destroy()
        turing_alg_wid.button_right.destroy()
        turing_alg_wid.button_left.destroy()

        start_control_turing(dict_windows)


def read_and_create_task(turing_alg_obj, turing_alg_wid, number_task):
    with open("LEARNING_TURING.json", encoding='utf-8') as f:
        example_info = json.load(f)

    list_tasks = []
    for dct in example_info:
        if dct["type"] == number_task:
            list_tasks.append(dct)

    number_option = randint(0, len(list_tasks) - 1)
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

    if number_task == 5:
        num_row = current_tasks.get("num_cell_row")
        num_col = current_tasks.get("num_cell_col")
        cell = turing_alg_obj.table_rules[num_row][num_col]
        cell["state"] = "normal"
        turing_alg_wid.entry_answer_stud_third = cell

    turing_alg_wid.list_true_answer.append(current_tasks.get("answer"))


def creating_infinity_tape(turing_alg_obj, turing_alg_wid):
    place_x = 0
    turing_alg_obj.pointer_index = 0

    for ind in range(-9, 10):
        symbol = Tk.StringVar(turing_alg_wid.frame_infinity_tape)
        symbol.set(" ")

        current_opt_menu = Tk.OptionMenu(turing_alg_wid.frame_infinity_tape, symbol, *turing_alg_obj.alphabetical)
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, turing_alg_obj.alphabetical)
        turing_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=turing_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"), background="white")
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

    if turing_alg_wid.text_task_condition:
        turing_alg_wid.text_task_condition.delete("1.0", "end")

    turing_alg_wid.output_elm_ids = [-9, 9]

    delete_rules_table(turing_alg_obj)

    for elem in turing_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    turing_alg_wid.list_label_ind.clear()

    if turing_alg_wid.frame_infinity_tape:
        delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
        turing_alg_wid.infinity_tape.clear()


def create_random_rule_for_task():
    return random.choice(string.ascii_letters)+random.choice(['<', '>', '.'])+str(random.randint(0, 25))


def first_task_turing(dict_windows, widgets, entry_surname_stud=None, surname_stud=None):
    if entry_surname_stud:
        if entry_surname_stud.get() == "":
            messagebox.showerror(title="Не заполнены данные",
                             message="Для продолжения контроля необходимо заполнить фамилию и имя",
                             parent=dict_windows["window_control_turing"])
            return
        else:
            surname_stud = entry_surname_stud.get()

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 1", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=50)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_control_turing)
    label_fon = Tk.Label(window_control_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_control_turing, highlightthickness=0, width=240, height=450, background="white", border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)
    widgets.append(canvas)

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

    label_description_task = Tk.Label(master=window_control_turing, width=50, text=FIRST_TASK,
                                      justify="center", font=("Gabriola", "28"), background="white")
    label_description_task.place(x=300, y=200)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_task()}
    true_answer = [dict_rule['rule'][0]]
    if dict_rule['rule'][1] == "<":
        true_answer.append('влево')
    elif dict_rule['rule'][1] == ">":
        true_answer.append('вправо')
    else:
        true_answer.append('не двигаем')
    true_answer.append(dict_rule['rule'][2:])

    label_rule = Tk.Label(master=window_control_turing, width=15, text=dict_rule['rule'],
                          font=("Cambria", "30"), justify="center", background="white")
    label_rule.place(x=500, y=275)
    widgets.append(label_rule)

    frame_questions = Tk.Frame(master=window_control_turing, width=800, height=500,
                               background="white", border=0)
    frame_questions.place(x=150, y=325)
    widgets.append(frame_questions)

    list_answer_stud = []

    label_first_question = Tk.Label(master=frame_questions, width=50, text="На какой символ заменяем?",
                                    font=("Gabriola", "24"), background="white", justify="left")
    label_first_question.place(x=100, y=0)
    widgets.append(label_first_question)
    entry_first_question = Tk.Entry(master=frame_questions, width=10, font=('Cambria', 16, 'bold'), relief="raised")
    entry_first_question.place(x=600, y=10)
    entry_first_question.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_first_question)
    list_answer_stud.append(entry_first_question)

    label_second_question = Tk.Label(master=frame_questions, width=50, justify="left", text="Куда передвигаем каретку?",
                                     font=("Gabriola", "24"), background="white")
    label_second_question.place(x=100, y=50)
    widgets.append(label_second_question)
    variable = Tk.StringVar(frame_questions)
    variable.set('выбрать')
    answers = ['влево', 'вправо', 'не двигаем']
    option_menu_answer = Tk.OptionMenu(frame_questions, variable, *answers)
    option_menu_answer.config(width=10, font=("Cambria", "16"), justify="left")
    option_menu_answer.place(x=600, y=60)
    widgets.append(option_menu_answer)

    label_third_question = Tk.Label(master=frame_questions, width=50, justify="left",
                                    text="В какое состояние переходим?", font=("Gabriola", "24"), background="white")
    label_third_question.place(x=100, y=100)
    widgets.append(label_third_question)
    entry_third_question = Tk.Entry(master=frame_questions, width=10, font=('Cambria', 16, 'bold'), relief="raised")
    entry_third_question.place(x=600, y=110)
    entry_third_question.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_third_question)
    list_answer_stud.append(entry_third_question)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control_two.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_control_turing)
    label_fon = Tk.Label(window_control_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas_two = Tk.Canvas(master=window_control_turing, highlightthickness=0, width=240, height=162, background="white",
                       border=0)
    canvas_two.place(x=300, y=750)
    canvas_two.create_image(0, 0, anchor="nw", image=photo_fon)
    widgets.append(canvas_two)

    label_true_tasks = Tk.Label(master=window_control_turing, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: second_task_turing(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                               list_answer_stud, surname_stud, variable))
    button_next.place(x=960, y=705)
    widgets.append(button_next)

    alphabetical = []
    infinity_tape = {}
    counter_states = 2
    output_elm_ids = [-9, 9]
    turing_alg_obj = TuringAlg(0, alphabetical, 1, counter_states)
    turing_alg_wid = ObjTuringAlg(infinity_tape, None, None, output_elm_ids,
                                  None, None, None)
    turing_alg_wid.list_true_answer.append(true_answer)


def create_text_second_task(dict_rule):
    number = random.randint(0, 3)
    if dict_rule['rule'][1] == '<':
        transition = 'передвигаем влево'
    elif dict_rule['rule'][1] == '>':
        transition = 'передвигаем вправо'
    else:
        transition = 'не передвигаем'

    if number == 0:
        return f"""	  Из текущего состояния переходим в состояние {dict_rule['rule'][2:]}, заменяем текущий элемент 
        на {dict_rule['rule'][0]}, каретку {transition}"""
    elif number == 1:
        return f"""   Элемент заменяем на {dict_rule['rule'][0]}, {transition} каретку, переходим 
        в состояние {dict_rule['rule'][2:]}"""
    elif number == 2:
        return f"""   Заменяем текущий элемент на {dict_rule['rule'][0]}, каретку {transition}, из текущего 
        состояния переходим в состояние {dict_rule['rule'][2:]}"""
    else:
        return f"""   Текущий элемент заменяем на {dict_rule['rule'][0]}, переходим в {dict_rule['rule'][2:]} 
        состояние, каретку {transition}"""


def second_task_turing(dict_windows, widgets, turing_alg_obj, turing_alg_wid, list_answer_first_task_stud, surname_stud,
                       variable):
    first_answer = [list_answer_first_task_stud[0].get(), variable.get(), list_answer_first_task_stud[1].get()]
    turing_alg_wid.list_answer_stud.append(first_answer)

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 2", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=50)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_control_turing)
    label_fon = Tk.Label(window_control_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_control_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)
    widgets.append(canvas)

    label_description_task = Tk.Label(master=window_control_turing, width=50, text=SECOND_TASK,
                                      justify="center", font=("Gabriola", "28"), background="white")
    label_description_task.place(x=300, y=200)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_task()}
    label_task = Tk.Label(master=window_control_turing, width=75, text=create_text_second_task(dict_rule),
                          justify="center", font=("Gabriola", "24"),
                          background="white")
    label_task.place(x=150, y=300)
    widgets.append(label_task)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "28"),
                            background="white")
    label_answer.place(x=450, y=450)
    widgets.append(label_answer)
    entry_answer = Tk.Entry(master=window_control_turing, width=15, font=('Cambria', 20, 'bold'), relief="raised")
    entry_answer.place(x=600, y=470)
    entry_answer.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_answer)

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

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: third_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                       entry_answer, surname_stud))
    button_next.place(x=960, y=705)
    widgets.append(button_next)
    turing_alg_wid.list_true_answer.append(dict_rule['rule'])


def third_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud, surname_stud):
    turing_alg_wid.list_answer_stud.append(entry_answer_stud.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)
    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 3", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=30)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_control_turing)
    label_fon = Tk.Label(window_control_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_control_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)

    turing_alg_wid.text_task_condition = Tk.Text(master=window_control_turing, width=75, height=6, font=("Cambria", "16"))
    turing_alg_wid.text_task_condition.place(x=250, y=150)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "28"),
                            background="white")
    label_answer.place(x=750, y=475)
    widgets.append(label_answer)

    entry_answer_stud = Tk.Entry(master=window_control_turing, width=10, font=('Cambria', 20, 'bold'), relief="raised")
    entry_answer_stud.place(x=900, y=490)
    entry_answer_stud.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_answer_stud)

    frame_table_rules = Tk.Frame(master=window_control_turing, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=50, y=475)
    turing_alg_wid.frame_table_rules = frame_table_rules

    frame_infinity_tape = Tk.Frame(master=window_control_turing, width=1140, height=100, background="white")
    frame_infinity_tape.place(x=30, y=350)
    turing_alg_wid.frame_infinity_tape = frame_infinity_tape

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_control_turing)
    label_point = Tk.Label(window_control_turing, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=41, background="white")
    label_point.place(x=547, y=0)

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_control_turing)
    label_right = Tk.Label(window_control_turing, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_control_turing, image=photo_right, background="white", width=1, height=6,
                             command=lambda: movement_right(turing_alg_obj, turing_alg_wid))
    button_right.place(x=1170, y=350, height=100, width=30)
    turing_alg_wid.button_right = button_right

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_control_turing)
    label_left = Tk.Label(window_control_turing, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_control_turing, image=photo_left, background="white", width=1, height=6,
                            command=lambda: movement_left(turing_alg_obj, turing_alg_wid))
    button_left.place(x=0, y=350, height=100, width=30)
    turing_alg_wid.button_left = button_left

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

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: fourth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                        entry_answer_stud, surname_stud, canvas))
    button_next.place(x=960, y=705)
    widgets.append(button_next)

    read_and_create_task(turing_alg_obj, turing_alg_wid, 3)


def fourth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud, surname_stud, canvas):
    turing_alg_wid.list_answer_stud.append(entry_answer_stud.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 4", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=30)
    widgets.append(label_number_task)

    label_answer = Tk.Label(master=window_control_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "28"),
                            background="white")
    label_answer.place(x=750, y=475)
    widgets.append(label_answer)

    entry_answer_stud = Tk.Entry(master=window_control_turing, width=10, font=('Cambria', 20, 'bold'), relief="raised")
    entry_answer_stud.place(x=900, y=490)
    entry_answer_stud.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_answer_stud)

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

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_control_turing)
    label_next = Tk.Label(window_control_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_control_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: fifth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud, surname_stud, canvas))
    button_next.place(x=960, y=705)
    widgets.append(button_next)


def change(turing_alg_wid, val):
    turing_alg_wid.var = val


def fifth_task(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud, surname_stud, canvas):
    turing_alg_wid.list_answer_stud.append(entry_answer_stud.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    label_number_task = Tk.Label(master=window_control_turing, text="Задание 5", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=30)
    widgets.append(label_number_task)

    img_end = Image.open(Path.cwd() / "Image" / "end.png")
    photo_end = ImageTk.PhotoImage(img_end, master=window_control_turing)
    label_end = Tk.Label(window_control_turing, image=photo_end)
    label_end.image = photo_end
    button_end = Tk.Button(master=window_control_turing, text="Завершить тест  ", image=photo_end, compound="right",
                           font=("Gabriola", "20"), width=210, height=50, background="white", relief="flat",
                           cursor="hand2",
                           command=lambda: test_results(dict_windows, widgets, turing_alg_obj, turing_alg_wid,
                                                        entry_answer_stud, surname_stud, canvas))
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


def test_results(dict_windows, widgets, turing_alg_obj, turing_alg_wid, entry_answer_stud, surname_stud, canvas):
    turing_alg_wid.list_answer_stud.append(turing_alg_wid.entry_answer_stud_third.get())

    cleaning_widgets(turing_alg_obj, turing_alg_wid)
    turing_alg_wid.frame_infinity_tape.destroy()
    turing_alg_wid.frame_table_rules.destroy()
    turing_alg_wid.text_task_condition.destroy()
    turing_alg_wid.button_right.destroy()
    turing_alg_wid.button_left.destroy()
    canvas.destroy()

    widgets = destroy_widgets(widgets)
    window_control_turing = dict_windows["window_control_turing"]

    counter = 0
    first_count = 0
    str_result = ''
    for i in range(len(turing_alg_wid.list_answer_stud[0])):
        if turing_alg_wid.list_answer_stud[0][i] == turing_alg_wid.list_true_answer[0][i]:
            first_count += 1
    if first_count == 3:
        counter += 1
        str_result += '+'
    else:
        str_result += '-'
    for i in range(1, len(turing_alg_wid.list_answer_stud)):
        if turing_alg_wid.list_answer_stud[i] == turing_alg_wid.list_true_answer[i]:
            counter += 1
            str_result += '+'
            if i == 4:
                counter += 1
                str_result += '+'
        else:
            str_result += '-'
            if i == 4:
                str_result += '-'

    file = open("Result_Control_TURING.txt", "a+", encoding='utf-8')
    file.write(f'{surname_stud} баллы: {counter} {str_result}\n')
    file.close()

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
                              relief="flat", cursor="hand2", command=lambda: first_task_turing(dict_windows, widgets, None, surname_stud))
    button_repeat.place(x=980, y=690)
    widgets.append(button_repeat)
