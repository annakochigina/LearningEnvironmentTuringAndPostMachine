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

LEARN_TURING = text.CONST_LEARN_TURING
FIRST_TASK = text.CONST_LEARN_FIRST_TASK_TURING
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

    label_number_task = Tk.Label(master=window_learning_turing, width=80, text="Задание 1", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat")
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_turing, width=100, text=FIRST_TASK,
                                       justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_task()}
    label_rule = Tk.Label(master=window_learning_turing, width=70, justify="center", text=dict_rule['rule'], font=("Times New Roman", "24"), background="white")
    label_rule.place(x=20, y=150)
    widgets.append(label_rule)

    frame_questions = Tk.Frame(master=window_learning_turing, width=1000, height=400,
                                         background="white", border=15)
    frame_questions.place(x=100, y=200)
    widgets.append(frame_questions)

    label_first_question = Tk.Label(master=frame_questions, width=50, justify="left", text="На какой символ заменяем?", font=("Gabriola", "20"), background="white")
    label_first_question.place(x=0,y=0)
    widgets.append(label_first_question)
    entry_first_question = Tk.Entry(master=frame_questions, width=10, font=('Arial', 16, 'bold'), relief="raised")
    entry_first_question.place(x=450, y=10)
    widgets.append(entry_first_question)

    label_second_question = Tk.Label(master=frame_questions, width=50, justify="left", text="Куда передвигаем указатель?", font=("Gabriola", "20"), background="white")
    label_second_question.place(x=0,y=50)
    widgets.append(label_second_question)
    entry_second_question = Tk.Entry(master=frame_questions, width=10, font=('Arial', 16, 'bold'), relief="raised")
    entry_second_question.place(x=450, y=60)
    widgets.append(entry_second_question)

    label_third_question = Tk.Label(master=frame_questions, width=50, justify="left", text="В какое состояние переходим?", font=("Gabriola", "20"), background="white")
    label_third_question.place(x=0,y=100)
    widgets.append(label_third_question)
    entry_third_question = Tk.Entry(master=frame_questions, width=10, font=('Arial', 16, 'bold'), relief="raised")
    entry_third_question.place(x=450, y=110)
    widgets.append(entry_third_question)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "20"), background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=15, height=1, font=("Arial", "12", "italic"), background="white",
                             cursor="hand2", command=lambda : check_first_task(dict_rule, label_true_tasks, entry_first_question, entry_second_question, entry_third_question))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", width=15, height=1, font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2", command=lambda: restart_first_task(dict_rule, label_rule, label_true_tasks, entry_first_question, entry_second_question, entry_third_question))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2", command=lambda: second_task_learn(dict_windows, widgets))
    button_next.place(x=950, y=705)
    widgets.append(button_next)


def create_random_rule_for_task():
    return random.choice(string.ascii_letters+string.digits)+random.choice(['<', '>', '.'])+str(random.randint(0, 25))


def check_first_task(dict_rule, label_true_tasks, entry_first_question, entry_second_question, entry_third_question):
    count_true = 0

    if entry_first_question.get() == "" or entry_second_question.get() == "" or entry_third_question.get() == "":
        return messagebox.showerror(title="Ошибка", message="Даны не все ответы", parent=entry_third_question)
    if entry_first_question.get() == dict_rule['rule'][0]:
        entry_first_question.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
    else:
        entry_first_question.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
    if entry_second_question.get() == dict_rule['rule'][1]:
        entry_second_question.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
    else:
        entry_second_question.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
    if entry_third_question.get() == dict_rule['rule'][2:]:
        entry_third_question.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
    else:
        entry_third_question.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
    print(count_true)
    if count_true == 3:
        label_true_tasks.config(text="Молодец! Ты верно выполнил задание!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуй ещё раз!")


def restart_first_task(dict_rule, label_rule, label_true_tasks, entry_first_question, entry_second_question, entry_third_question):
    entry_first_question.delete("0", "end")
    entry_first_question.config(highlightbackground="white", highlightcolor="white")
    entry_second_question.delete("0", "end")
    entry_second_question.config(highlightbackground="white", highlightcolor="white")
    entry_third_question.delete("0", "end")
    entry_third_question.config(highlightbackground="white", highlightcolor="white")
    label_true_tasks.config(text="")

    dict_rule['rule'] = create_random_rule_for_task()
    label_rule.config(text=dict_rule['rule'])


def second_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_turing = dict_windows["window_learning_turing"]

    label_number_task = Tk.Label(master=window_learning_turing, width=80, text="Задание 2", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_turing)
    label_exit = Tk.Label(window_learning_turing, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_turing, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat")
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_turing, width=100, text=SECOND_TASK,
                                      justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_task()}
    print(dict_rule['rule'])

    label_task = Tk.Label(master=window_learning_turing, width=100, text=create_text_second_task(dict_rule), justify="left", font=("Gabriola", "18"),
                                background="white")
    label_task.place(x=50, y=200)
    widgets.append(label_task)
    entry_answer = Tk.Entry(master=window_learning_turing, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer.place(x=350, y=350)
    widgets.append(entry_answer)

    label_true_tasks = Tk.Label(master=window_learning_turing, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    button_verification = Tk.Button(master=window_learning_turing, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_second_task(dict_rule, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_turing, text="Повторить", width=15, height=1,
                               font=("Arial", "12", "italic"), background="white",
                               cursor="hand2",
                               command=lambda: restart_second_task(dict_rule, entry_answer, label_task, label_true_tasks))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_turing)
    label_next = Tk.Label(window_learning_turing, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_turing, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2")
    button_next.place(x=950, y=705)
    widgets.append(button_next)


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
        на {dict_rule['rule'][0]}, указатель {transition}"""
    elif number == 1:
        return f"""   Элемент заменяем на {dict_rule['rule'][0]}, {transition} указатель, переходим 
        в состояние {dict_rule['rule'][2:]}"""
    elif number == 2:
        return f"""   Заменяем текущий элемент на {dict_rule['rule'][0]}, указатель {transition}, из текущего 
        состояния переходим в состояние {dict_rule['rule'][2:]}"""
    else:
        return f"""   Текущий элемент заменяем на {dict_rule['rule'][0]}, переходим в {dict_rule['rule'][2:]} 
        состояние, указатель {transition}"""


def check_second_task(dict_rule, entry_answer, label_true_tasks):
    if entry_answer.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже ты забыл написать ответ..", parent=entry_answer)

    if entry_answer.get() == dict_rule['rule']:
        entry_answer.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        label_true_tasks.config(text="Молодец! Ты верно выполнил задание!")
    else:
        entry_answer.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуй ещё раз!")


def restart_second_task(dict_rule, entry_answer, label_task, label_true_tasks):
    entry_answer.delete("0", "end")
    entry_answer.config(highlightbackground="white", highlightcolor="white")
    label_true_tasks.config(text="")

    dict_rule['rule'] = create_random_rule_for_task()
    label_task.config(text=create_text_second_task(dict_rule))
