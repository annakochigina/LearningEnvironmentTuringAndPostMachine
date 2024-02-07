import tkinter
import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk
from classes.MyOptionMenu import MyOptionMenu
from classes.PostAlg import PostAlg
from classes.ObjPostAlg import ObjPostAlg
import re, os, random, string
import const.text as text
from PIL import Image, ImageTk
from pathlib import Path
import tkinter.filedialog as fd
import json

LEARN_POST = text.CONST_LEARN
FIRST_TASK = text.CONST_LEARN_FIRST_TASK
SECOND_TASK = text.CONST_LEARN_SECOND_TASK_TURING

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def return_window_for_algorithms(dict_windows):
    if (messagebox.askokcancel("Выход из обучения", "Вы уверены, что хотите выйти из обучения?",
                               parent=dict_windows["window_learning_post"])):
        dict_windows["window_learning_post"].destroy()
        dict_windows["window_for_algorithms"].deiconify()


def destroy_widgets(widgets):
    for obj in widgets:
        obj.destroy()
    return []


def create_learning_post(dict_windows):
    window_learning_post = Tk.Tk()
    window_learning_post_width_center = (window_learning_post.winfo_screenwidth()) // 2 - 600
    window_learning_post_height_center = (window_learning_post.winfo_screenheight()) // 2 - 375
    window_learning_post.geometry(
        "1200x750+{}+{}".format(window_learning_post_width_center, window_learning_post_height_center))
    window_learning_post.resizable(width=False, height=False)
    window_learning_post.config(bg="white")
    dict_windows["window_learning_post"] = window_learning_post
    window_learning_post.title("Обучение - машина Поста")

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, relief="flat", background="white", width=40,
                            height=40, cursor="hand2", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)

    widgets = []

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, width=40, height=40, relief="flat",
                            background="white", cursor="hand2",
                            command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_start = Tk.Label(master=window_learning_post, text="Обучение", justify="center", width=35,
                           background=rgb_hack((1, 116, 64)), font=("Gabriola", "40"))
    label_start.place(x=200, y=200)
    widgets.append(label_start)

    frame_description_learn = Tk.Frame(master=window_learning_post, width=775, height=400,
                                         background=rgb_hack((1, 116, 64)), border=15)
    frame_description_learn.place(x=200, y=350)
    widgets.append(frame_description_learn)

    label_description_learn = Tk.Label(master=frame_description_learn, width=65, height=7, text=LEARN_POST,
                                         justify="center", font=("Gabriola", "20"), background="white")
    label_description_learn.place(x=10, y=10)
    widgets.append(label_description_learn)

    img_start = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_start = ImageTk.PhotoImage(img_start, master=window_learning_post)
    label_start = Tk.Label(window_learning_post, image=photo_start)
    label_start.image = photo_start
    button_start = Tk.Button(master=window_learning_post, text="Начать обучение  ", image=photo_start,
                             compound="right", width=200, height=20, font=("Gabriola", "20"), background="white",
                             relief="flat", cursor="hand2", command=lambda: first_task_learn(dict_windows, widgets))
    button_start.place(x=980, y=705)
    widgets.append(button_start)

    window_learning_post.protocol("WM_DELETE_WINDOW", lambda: return_window_for_algorithms(dict_windows))
    

def first_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_post = dict_windows["window_learning_post"]

    label_number_task = Tk.Label(master=window_learning_post, width=80, text="Задание 1", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda:
                            return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_post, width=100, text=FIRST_TASK,
                                       justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_double_digit()}
    label_rule = Tk.Label(master=window_learning_post, width=70, justify="center", text=dict_rule['rule'],
                          font=("Times New Roman", "24"), background="white")
    label_rule.place(x=20, y=150)
    widgets.append(label_rule)

    frame_questions = Tk.Frame(master=window_learning_post, width=1000, height=400,
                                         background="white", border=15)
    frame_questions.place(x=100, y=200)
    widgets.append(frame_questions)

    label_first_question = Tk.Label(master=frame_questions, width=50, justify="left", text="Какая команда выполняется?",
                                    font=("Gabriola", "20"), background="white")
    label_first_question.place(x=0, y=0)
    widgets.append(label_first_question)

    variable = Tk.StringVar(frame_questions)
    variable.set('выберете вариант ответа')

    answers = ['передвигает каретку влево', 'передвигает каретку вправо', 'стирает пометку', 'ставит пометку', 'останавливает программу', 'проверяет наличие пометки']
    widgets_frame_question = []

    option_menu_answer = Tk.OptionMenu(frame_questions, variable, *answers, command=lambda x: create_second_path_first_task(x, frame_questions, widgets_frame_question))
    option_menu_answer.config(width=25, font=("Gabriola", "14"))
    option_menu_answer.place(x=425, y=0)
    widgets.append(option_menu_answer)

    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1, font=("Arial", "12", "italic"), background="white",
                             cursor="hand2", command=lambda : check_first_task(dict_rule, label_true_tasks, entry_first_question, entry_second_question, entry_third_question))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_post, text="Повторить", width=15, height=1, font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2", command=lambda: restart_first_task(dict_rule, label_rule, label_true_tasks, entry_first_question, entry_second_question, entry_third_question))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_post)
    label_next = Tk.Label(window_learning_post, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_post, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2", command=lambda: second_task_learn(dict_windows, widgets))
    button_next.place(x=950, y=705)
    widgets.append(button_next)


def create_random_rule_for_double_digit():
    command = random.choice(['<', '>', '1', '0', '?', '.'])
    if command != '?' and command != '.':
        n = random.randint(1, 25)
        return f'{command} {n}'
    elif command == '?':
        n, m = random.randint(1, 25), random.randint(1, 25)
        while n == m:
            m = random.randint(1, 25)
        return f'{command} {n}, {m}'
    return command


def create_second_path_first_task(variable, frame, widgets_frame_question):

    for elem in widgets_frame_question:
        elem.destroy()
    if variable != 'останавливает программу' and variable != 'проверяет наличие пометки':
        label_question = Tk.Label(master=frame, width=50, justify="left",
                                        text="На какую строку осуществляется переход?",
                                        font=("Gabriola", "20"), background="white")
        label_question.place(x=0, y=50)
        widgets_frame_question.append(label_question)

        entry_answer = Tk.Entry(master=frame, width=10, font=('Arial', 16, 'bold'), relief="raised")
        entry_answer.place(x=500, y=60)
        widgets_frame_question.append(entry_answer)
