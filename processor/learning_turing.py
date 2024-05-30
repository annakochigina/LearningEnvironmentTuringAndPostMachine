import tkinter
import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk
from classes.MyOptionMenu import MyOptionMenu
from classes.TuringAlg import TuringAlg
from classes.ObjTuringAlg import ObjTuringAlg
import re, os, random, string
import const.text as text
from PIL import Image, ImageTk
from pathlib import Path
import tkinter.filedialog as fd
import json

LEARN_TURING = text.CONST_LEARN
FIRST_TASK = text.CONST_LEARN_FIRST_TASK
SECOND_TASK = text.CONST_LEARN_SECOND_TASK_TURING


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def return_window_for_algorithms(dict_windows):
    if (messagebox.askokcancel("Выход из обучения", "Вы уверены, что хотите выйти из обучения?",
                               parent=dict_windows["window_learning_turing"])):
        dict_windows["window_learning_turing"].destroy()
        dict_windows["window_for_algorithms"].deiconify()


def destroy_widgets(widgets):
    for obj in widgets:
        obj.destroy()
    return []


def create_learning_turing(dict_windows):
    window_learning_turing = Tk.Tk()
    window_learning_turing_width_center = (window_learning_turing.winfo_screenwidth()) // 2 - 600
    window_learning_turing_height_center = (window_learning_turing.winfo_screenheight()) // 2 - 375
    window_learning_turing.geometry(
        "1200x750+{}+{}".format(window_learning_turing_width_center, window_learning_turing_height_center))
    window_learning_turing.resizable(width=False, height=False)
    window_learning_turing.config(bg="white")
    dict_windows["window_learning_turing"] = window_learning_turing
    window_learning_turing.title("Обучение - машина Тьюринга")

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, relief="flat", background="white", width=40,
                            height=40, cursor="hand2", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)

    widgets = []

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, relief="flat",
                            background="white", cursor="hand2",
                            command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_start = Tk.Label(master=window_learning_turing, text="Обучение", justify="center", width=35,
                           background=rgb_hack((1, 116, 64)), font=("Gabriola", "40"))
    label_start.place(x=200, y=200)
    widgets.append(label_start)

    frame_description_learn = Tk.Frame(master=window_learning_turing, width=775, height=400,
                                         background=rgb_hack((1, 116, 64)), border=15)
    frame_description_learn.place(x=200, y=350)
    widgets.append(frame_description_learn)

    label_description_learn = Tk.Label(master=frame_description_learn, width=65, height=7, text=LEARN_TURING,
                                         justify="center", font=("Gabriola", "20"), background="white")
    label_description_learn.place(x=10, y=10)
    widgets.append(label_description_learn)

    img_start = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_start = ImageTk.PhotoImage(img_start, master=window_learning_turing)
    label_start = Tk.Label(window_learning_turing, image=photo_start)
    label_start.image = photo_start
    button_start = Tk.Button(master=window_learning_turing, text="Начать обучение  ", image=photo_start,
                             compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                             relief="flat", cursor="hand2", command=lambda: first_task_learn(dict_windows, widgets))
    button_start.place(x=980, y=705)
    widgets.append(button_start)

    window_learning_turing.protocol("WM_DELETE_WINDOW", lambda: return_window_for_algorithms(dict_windows))


def first_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_turing = dict_windows["window_learning_turing"]

    label_number_task = Tk.Label(master=window_learning_turing, text="Задание 1", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=50)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_learning_turing)
    label_fon = Tk.Label(window_learning_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_learning_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)
    widgets.append(canvas)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_turing, width=50, text=FIRST_TASK,
                                      justify="center", font=("Gabriola", "28"), background="white")
    label_description_task.place(x=300, y=200)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_task()}

    label_rule = Tk.Label(master=window_learning_turing, width=15, text=dict_rule['rule'],
                          font=("Cambria", "30"), justify="center", background="white")
    label_rule.place(x=500, y=275)
    widgets.append(label_rule)

    frame_questions = Tk.Frame(master=window_learning_turing, width=850, height=500,
                               background="white", border=0)
    frame_questions.place(x=150, y=325)
    widgets.append(frame_questions)

    list_entry_answer = []

    label_first_question = Tk.Label(master=frame_questions, width=50, text="На какой символ заменяем?",
                                    font=("Gabriola", "24"), background="white", justify="left")
    label_first_question.place(x=100, y=0)
    widgets.append(label_first_question)
    entry_first_question = Tk.Entry(master=frame_questions, width=10, font=('Cambria', 16, 'bold'), relief="raised")
    entry_first_question.place(x=600, y=10)
    entry_first_question.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_first_question)
    list_entry_answer.append(entry_first_question)

    label_second_question = Tk.Label(master=frame_questions, width=50, justify="left", text="Куда передвигаем каретку?",
                                     font=("Gabriola", "24"), background="white")
    label_second_question.place(x=100, y=50)
    widgets.append(label_second_question)
    variable = Tk.StringVar(frame_questions)
    variable.set('выбрать вариант')
    answers = ['влево', 'вправо', 'не двигаем']
    option_menu_answer = Tk.OptionMenu(frame_questions, variable, *answers)
    option_menu_answer.config(width=15, font=("Cambria", "16"), justify="left")
    option_menu_answer.place(x=600, y=60)
    widgets.append(option_menu_answer)
    list_entry_answer.append(variable)

    label_third_question = Tk.Label(master=frame_questions, width=50, justify="left",
                                    text="В какое состояние переходим?", font=("Gabriola", "24"), background="white")
    label_third_question.place(x=100, y=100)
    widgets.append(label_third_question)
    entry_third_question = Tk.Entry(master=frame_questions, width=10, font=('Cambria', 16, 'bold'), relief="raised")
    entry_third_question.place(x=600, y=110)
    entry_third_question.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_third_question)
    list_entry_answer.append(entry_third_question)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "24"), background="white")
    label_true_tasks.place(x=250, y=600)
    widgets.append(label_true_tasks)

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=20, height=1, font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                             cursor="hand2", relief="flat", command=lambda: check_first_task(dict_rule, label_true_tasks, list_entry_answer, option_menu_answer))
    button_verification.place(x=650, y=700)
    widgets.append(button_verification)

    img_next = Image.open(Path.cwd() / "Image" / "repeat.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", image=photo_next, compound="left", width=225, height=35, font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                                    cursor="hand2", relief="flat", command=lambda: restart_first_task(dict_rule, label_rule, label_true_tasks, list_entry_answer, option_menu_answer))
    button_restart.place(x=375, y=700)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=300, height=35, font=("Arial", "16", "italic"), background="white",
                            cursor="hand2", relief="flat", command=lambda: second_task_learn(dict_windows, widgets))
    button_next.place(x=900, y=700)
    widgets.append(button_next)


def create_random_rule_for_task():
    return random.choice(string.ascii_letters+string.digits)+random.choice(['<', '>', '.'])+str(random.randint(0, 25))


def check_first_task(dict_rule, label_true_tasks, list_entry_answer, option_menu_answer):
    count_true = 0

    true_answer = ''
    if dict_rule['rule'][1] == "<":
        true_answer = 'влево'
    elif dict_rule['rule'][1] == ">":
        true_answer = 'вправо'
    else:
        true_answer = 'не двигаем'

    if list_entry_answer[0].get() == "" or list_entry_answer[1].get() == "выбрать вариант" or list_entry_answer[2].get() == "":
        return messagebox.showerror(title="Ошибка", message="Ответьте на все вопросы", parent=list_entry_answer[0])
    if list_entry_answer[0].get() == dict_rule['rule'][0]:
        list_entry_answer[0].config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
    else:
        list_entry_answer[0].config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
    if list_entry_answer[1].get() == true_answer:
        option_menu_answer.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
    else:
        option_menu_answer.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
    if list_entry_answer[2].get() == dict_rule['rule'][2:]:
        list_entry_answer[2].config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
    else:
        list_entry_answer[2].config(highlightthickness=2, highlightbackground="red", highlightcolor="red")

    if count_true == 3:
        label_true_tasks.config(text="Отлично! Задание выполнено верно!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуйте ещё раз!")


def restart_first_task(dict_rule, label_rule, label_true_tasks, list_entry_stud, option_menu_answer):
    list_entry_stud[0].delete("0", "end")
    list_entry_stud[0].config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    list_entry_stud[1].set("выбрать вариант")
    option_menu_answer.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    list_entry_stud[2].delete("0", "end")
    list_entry_stud[2].config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    label_true_tasks.config(text="")

    dict_rule['rule'] = create_random_rule_for_task()
    label_rule.config(text=dict_rule['rule'])


def second_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_turing = dict_windows["window_learning_turing"]

    label_number_task = Tk.Label(master=window_learning_turing, text="Задание 2", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=50)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_learning_turing)
    label_fon = Tk.Label(window_learning_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_learning_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)
    widgets.append(canvas)

    label_description_task = Tk.Label(master=window_learning_turing, width=50, text=SECOND_TASK,
                                      justify="center", font=("Gabriola", "28"), background="white")
    label_description_task.place(x=300, y=200)
    widgets.append(label_description_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    dict_rule = {'rule': create_random_rule_for_task()}

    label_task = Tk.Label(master=window_learning_turing, width=75, text=create_text_second_task(dict_rule),
                          justify="center", font=("Gabriola", "24"),
                          background="white")
    label_task.place(x=150, y=300)
    widgets.append(label_task)

    label_answer = Tk.Label(master=window_learning_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "28"),
                            background="white")
    label_answer.place(x=450, y=450)
    widgets.append(label_answer)
    entry_answer = Tk.Entry(master=window_learning_turing, width=15, font=('Cambria', 20, 'bold'), relief="raised")
    entry_answer.place(x=600, y=470)
    entry_answer.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    widgets.append(entry_answer)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "24"),
                                background="white")
    label_true_tasks.place(x=250, y=600)
    widgets.append(label_true_tasks)

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=20, height=1,
                                    font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                                    cursor="hand2", relief="flat",
                                    command=lambda: check_second_task(dict_rule, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=700)
    widgets.append(button_verification)

    img_next = Image.open(Path.cwd() / "Image" / "repeat.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", width=225, height=35,
                               image=photo_next, compound="left", font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                               cursor="hand2", relief="flat",
                               command=lambda: restart_second_task(dict_rule, entry_answer, label_task, label_true_tasks))
    button_restart.place(x=375, y=700)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=300, height=35, font=("Arial", "16", "italic"), background="white",
                            cursor="hand2", relief="flat", command=lambda: third_task_learn(dict_windows, widgets))
    button_next.place(x=900, y=700)
    widgets.append(button_next)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_turing)
    label_previos = Tk.Label(window_learning_turing, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_turing, text="Предыдущее задание  ", image=photo_previos,
                            compound="left", width=300, height=35, font=("Arial", "16", "italic"), background="white",
                            cursor="hand2", relief="flat", command=lambda: first_task_learn(dict_windows, widgets))
    button_previos.place(x=60, y=700)
    widgets.append(button_previos)


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


def check_second_task(dict_rule, entry_answer, label_true_tasks):
    if entry_answer.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже вы забыли написать ответ..", parent=entry_answer)

    if entry_answer.get() == dict_rule['rule']:
        entry_answer.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        label_true_tasks.config(text="Отлично! Задание выполнено верно!")
    else:
        entry_answer.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуйте ещё раз!")


def restart_second_task(dict_rule, entry_answer, label_task, label_true_tasks):
    entry_answer.delete("0", "end")
    entry_answer.config(highlightthickness=2, highlightbackground="black", highlightcolor="black")
    label_true_tasks.config(text="")

    dict_rule['rule'] = create_random_rule_for_task()
    label_task.config(text=create_text_second_task(dict_rule))


def third_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_turing = dict_windows["window_learning_turing"]

    label_number_task = Tk.Label(master=window_learning_turing, text="Задание 3", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=30)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_learning_turing)
    label_fon = Tk.Label(window_learning_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_learning_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)

    text_task_condition = Tk.Text(master=window_learning_turing, width=75, height=6,
                                                 font=("Cambria", "16"))
    text_task_condition.place(x=250, y=150)
    widgets.append(text_task_condition)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "24"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    label_answer = Tk.Label(master=window_learning_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    frame_answer = Tk.Frame(master=window_learning_turing, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer.place(x=1, y=1)
    widgets.append(entry_answer)

    list_true_answer = []

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=20, height=1,
                                    font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                                    cursor="hand2", relief="flat",
                                    command=lambda: check_third_task(list_true_answer, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=700)
    widgets.append(button_verification)

    img_next = Image.open(Path.cwd() / "Image" / "repeat.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", width=225, height=35,
                               image=photo_next, compound="left", font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                               cursor="hand2", relief="flat",
                               command=lambda: restart_third_task(list_true_answer, label_true_tasks, entry_answer, turing_alg_obj, turing_alg_wid))
    button_restart.place(x=375, y=700)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=300, height=35, font=("Arial", "16", "italic"), background="white",
                            cursor="hand2", relief="flat", command=lambda: fourth_task_learn(dict_windows, widgets))
    button_next.place(x=900, y=700)
    widgets.append(button_next)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_turing)
    label_previos = Tk.Label(window_learning_turing, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_turing, text="Предыдущее задание  ", image=photo_previos,
                               compound="left", width=300, height=35, font=("Arial", "16", "italic"),
                               background="white", relief="flat",
                               cursor="hand2", command=lambda: second_task_learn(dict_windows, widgets))
    button_previos.place(x=60, y=700)
    widgets.append(button_previos)

    frame_table_rules = Tk.Frame(master=window_learning_turing, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=50, y=430)
    widgets.append(frame_table_rules)

    frame_infinity_tape = Tk.Frame(master=window_learning_turing, width=1140, height=100, background="white")
    frame_infinity_tape.place(x=30, y=275)
    widgets.append(frame_infinity_tape)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_learning_turing)
    label_point = Tk.Label(window_learning_turing, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40, background="white")
    label_point.place(x=547, y=0)
    widgets.append(label_point)

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_learning_turing)
    label_right = Tk.Label(window_learning_turing, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_learning_turing, width=1, height=6, image=photo_right,
                             command=lambda: movement_right(turing_alg_obj, turing_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)
    widgets.append(button_right)

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_learning_turing)
    label_left = Tk.Label(window_learning_turing, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_learning_turing, width=1, height=6, image=photo_left,
                            command=lambda: movement_left(turing_alg_obj, turing_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)
    widgets.append(button_left)

    alphabetical = []
    infinity_tape = {}
    counter_states = 2
    output_elm_ids = [-9, 9]
    turing_alg_obj = TuringAlg(0, alphabetical, 1, counter_states)
    turing_alg_wid = ObjTuringAlg(infinity_tape, frame_infinity_tape, frame_table_rules, output_elm_ids,
                                  text_task_condition, button_right, button_left)

    read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, 3)


def restart_third_task(list_true_answer, label_true_tasks, entry_answer, turing_alg_obj, turing_alg_wid):
    cleaning_widgets(turing_alg_obj, turing_alg_wid)
    label_true_tasks.config(text="")
    entry_answer.delete("0", "end")
    list_true_answer.clear()
    read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, 3)


def check_third_task(list_true_answer, entry_answer, label_true_tasks):
    if entry_answer.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже вы забыли написать ответ..", parent=entry_answer)
    # print(list_true_answer)
    if list_true_answer[0] == entry_answer.get():
        label_true_tasks.config(text="Отлично! Задание выполнено верно!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуйте ещё раз!")


def fourth_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_turing = dict_windows["window_learning_turing"]

    label_number_task = Tk.Label(master=window_learning_turing, text="Задание 4", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=30)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_learning_turing)
    label_fon = Tk.Label(window_learning_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_learning_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)

    text_task_condition = Tk.Text(master=window_learning_turing, width=75, height=6,
                                  font=("Cambria", "16"))
    text_task_condition.place(x=250, y=150)
    widgets.append(text_task_condition)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "24"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    label_answer = Tk.Label(master=window_learning_turing, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    frame_answer = Tk.Frame(master=window_learning_turing, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer.place(x=1, y=1)
    widgets.append(entry_answer)

    list_true_answer = []

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=20, height=1,
                                    font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                                    cursor="hand2", relief="flat",
                                    command=lambda: check_fourth_task(list_true_answer, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=700)
    widgets.append(button_verification)

    img_next = Image.open(Path.cwd() / "Image" / "repeat.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", width=225, height=35,
                               image=photo_next, compound="left", font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                               cursor="hand2", relief="flat",
                               command=lambda: restart_fourth_task(list_true_answer, label_true_tasks, entry_answer, turing_alg_obj, turing_alg_wid))
    button_restart.place(x=375, y=700)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=300, height=35, font=("Arial", "16", "italic"), background="white",
                            cursor="hand2", relief="flat", command=lambda: fifth_task_learn(dict_windows, widgets))
    button_next.place(x=900, y=700)
    widgets.append(button_next)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_turing)
    label_previos = Tk.Label(window_learning_turing, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_turing, text="Предыдущее задание  ", image=photo_previos,
                               compound="left", width=300, height=35, font=("Arial", "16", "italic"),
                               background="white", relief="flat",
                               cursor="hand2", command=lambda: third_task_learn(dict_windows, widgets))
    button_previos.place(x=60, y=700)
    widgets.append(button_previos)

    frame_table_rules = Tk.Frame(master=window_learning_turing, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=50, y=430)
    widgets.append(frame_table_rules)

    frame_infinity_tape = Tk.Frame(master=window_learning_turing, width=1140, height=100, background="white")
    frame_infinity_tape.place(x=30, y=275)
    widgets.append(frame_infinity_tape)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_learning_turing)
    label_point = Tk.Label(window_learning_turing, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40, background="white")
    label_point.place(x=547, y=0)
    widgets.append(label_point)

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_learning_turing)
    label_right = Tk.Label(window_learning_turing, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_learning_turing, width=1, height=6, image=photo_right,
                             command=lambda: movement_right(turing_alg_obj, turing_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)
    widgets.append(button_right)

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_learning_turing)
    label_left = Tk.Label(window_learning_turing, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_learning_turing, width=1, height=6, image=photo_left,
                            command=lambda: movement_left(turing_alg_obj, turing_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)
    widgets.append(button_left)

    alphabetical = []
    infinity_tape = {}
    counter_states = 2
    output_elm_ids = [-9, 9]
    turing_alg_obj = TuringAlg(0, alphabetical, 1, counter_states)
    turing_alg_wid = ObjTuringAlg(infinity_tape, frame_infinity_tape, frame_table_rules, output_elm_ids,
                                  text_task_condition, button_right, button_left)

    read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, 4)


def restart_fourth_task(list_true_answer, label_true_tasks, entry_answer, turing_alg_obj, turing_alg_wid):
    cleaning_widgets(turing_alg_obj, turing_alg_wid)
    label_true_tasks.config(text="")
    entry_answer.delete("0", "end")
    turing_alg_wid.text_task_condition.delete("1.0", "end")
    list_true_answer.clear()
    read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, 4)


def check_fourth_task(list_true_answer, entry_answer, label_true_tasks):
    if entry_answer.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже вы забыли написать ответ..", parent=entry_answer)
    # print(list_true_answer)
    if list_true_answer[0] == entry_answer.get():
        label_true_tasks.config(text="Молодец! Ты верно выполнил задание!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуй ещё раз!")


def fifth_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_turing = dict_windows["window_learning_turing"]

    label_number_task = Tk.Label(master=window_learning_turing, text="Задание 5", width=25, justify="center",
                                 font=("Gabriola", "44"), background=rgb_hack((1, 116, 64)))
    label_number_task.place(x=375, y=30)
    widgets.append(label_number_task)

    img_fon = Image.open(Path.cwd() / "Image" / "fon_control.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_learning_turing)
    label_fon = Tk.Label(window_learning_turing, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_learning_turing, highlightthickness=0, width=240, height=450, background="white",
                       border=0)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)

    text_task_condition = Tk.Text(master=window_learning_turing, width=75, height=6,
                                  font=("Cambria", "16"))
    text_task_condition.place(x=250, y=150)
    widgets.append(text_task_condition)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_turing)
    label_previos = Tk.Label(window_learning_turing, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_turing, text="Предыдущее задание  ", image=photo_previos,
                               compound="left", width=300, height=35, font=("Arial", "16", "italic"),
                               background="white", relief="flat",
                               cursor="hand2", command=lambda: fourth_task_learn(dict_windows, widgets))
    button_previos.place(x=60, y=700)
    widgets.append(button_previos)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "24"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    list_true_answer = []

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=20, height=1,
                                    font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                                    cursor="hand2", relief="flat",
                                    command=lambda: check_fifth_task(list_true_answer, label_true_tasks, turing_alg_wid))
    button_verification.place(x=650, y=700)
    widgets.append(button_verification)

    img_next = Image.open(Path.cwd() / "Image" / "repeat.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", width=225, height=35,
                               image=photo_next, compound="left", font=("Arial", "16", "italic"), background=rgb_hack((1, 116, 64)),
                               cursor="hand2", relief="flat",
                               command=lambda: restart_fifth_task(list_true_answer, label_true_tasks, turing_alg_obj, turing_alg_wid))
    button_restart.place(x=350, y=700)
    widgets.append(button_restart)

    frame_table_rules = Tk.Frame(master=window_learning_turing, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=50, y=430)
    widgets.append(frame_table_rules)

    frame_infinity_tape = Tk.Frame(master=window_learning_turing, width=1140, height=100, background="white")
    frame_infinity_tape.place(x=30, y=275)
    widgets.append(frame_infinity_tape)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_learning_turing)
    label_point = Tk.Label(window_learning_turing, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40, background="white")
    label_point.place(x=547, y=0)
    widgets.append(label_point)

    img_right = Image.open(Path.cwd() / "Image" / "right.png")
    photo_right = ImageTk.PhotoImage(img_right, master=window_learning_turing)
    label_right = Tk.Label(window_learning_turing, image=photo_right)
    label_right.image = photo_right
    button_right = Tk.Button(master=window_learning_turing, width=1, height=6, image=photo_right,
                             command=lambda: movement_right(turing_alg_obj, turing_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)
    widgets.append(button_right)

    img_left = Image.open(Path.cwd() / "Image" / "left.png")
    photo_left = ImageTk.PhotoImage(img_left, master=window_learning_turing)
    label_left = Tk.Label(window_learning_turing, image=photo_left)
    label_left.image = photo_left
    button_left = Tk.Button(master=window_learning_turing, width=1, height=6, image=photo_left,
                            command=lambda: movement_left(turing_alg_obj, turing_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)
    widgets.append(button_left)

    alphabetical = []
    infinity_tape = {}
    counter_states = 2
    output_elm_ids = [-9, 9]
    turing_alg_obj = TuringAlg(0, alphabetical, 1, counter_states)
    turing_alg_wid = ObjTuringAlg(infinity_tape, frame_infinity_tape, frame_table_rules, output_elm_ids,
                                  text_task_condition, button_right, button_left)

    read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, 5)


def restart_fifth_task(list_true_answer, label_true_tasks, turing_alg_obj, turing_alg_wid):
    cleaning_widgets(turing_alg_obj, turing_alg_wid)
    label_true_tasks.config(text="")
    list_true_answer.clear()
    turing_alg_wid.text_task_condition.delete("1.0", "end")
    read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, 5)


def check_fifth_task(list_true_answer, label_true_tasks, turing_alg_wid):
    if turing_alg_wid.entry_answer_third.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже вы забыли написать ответ..", parent=turing_alg_wid.entry_answer_third)
    if list_true_answer[0] == turing_alg_wid.entry_answer_third.get():
        label_true_tasks.config(text="Отлично! Задание выполнено верно!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуйте ещё раз!")


def cleaning_widgets(turing_alg_obj, turing_alg_wid):
    turing_alg_wid.output_elm_ids = [-9, 9]

    delete_rules_table(turing_alg_obj)

    for elem in turing_alg_wid.list_label_ind:
        lbl = elem
        lbl.destroy()
    turing_alg_wid.list_label_ind.clear()

    delete_option_menu_from_frame(turing_alg_wid.frame_infinity_tape)
    turing_alg_wid.infinity_tape.clear()
    turing_alg_wid.text_task_condition.delete("1.0", "end")


def delete_option_menu_from_frame(frame: Tk.Frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tkinter.OptionMenu):
            widget.place(x=-1000, y=-1000)


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


def read_and_create_task(turing_alg_obj, turing_alg_wid, list_true_answer, number_task, num_row=None, num_col=None):
    with open("LEARNING_TURING.json", encoding='utf-8') as f:
        example_info = json.load(f)

    list_tasks = []
    for dct in example_info:
        if dct["type"] == number_task:
            list_tasks.append(dct)

    # number_option = random.randint(0, 4)
    number_option = random.randint(0, len(list_tasks) - 1)
    current_tasks = list_tasks[number_option]

    alphabetical_text = current_tasks.get("alphabetical")
    counter_states = current_tasks.get("counter_states")
    pointer_index = current_tasks.get("pointer_index")
    table_rules = current_tasks.get("table_rules")
    expression_info = current_tasks.get("expression")
    task_condition = current_tasks.get("task_condition")
    list_true_answer.append(current_tasks.get("answer"))

    turing_alg_obj.pointer_index = pointer_index
    turing_alg_obj.counter_states = counter_states
    turing_alg_obj.alphabetical = list(alphabetical_text)
    turing_alg_obj.alphabetical.append(" ")
    turing_alg_wid.text_task_condition.insert("end", task_condition)
    # label_description_task.config(text=task_condition)

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
        turing_alg_wid.entry_answer_third = cell

    # if number_task == 4:
    #     turing_alg_wid.lst_var = current_tasks.get("var")


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
