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
from random import randint

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

    label_true_tasks = Tk.Label(master=window_learning_post, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    variable = Tk.StringVar(frame_questions)
    variable.set('выберите вариант ответа')

    answers = ['передвигает каретку влево', 'передвигает каретку вправо', 'стирает пометку', 'ставит пометку', 'останавливает программу', 'проверяет наличие пометки']
    widgets_frame_question = []
    answers_stud_entry = []

    option_menu_answer = Tk.OptionMenu(frame_questions, variable, *answers, command=lambda x: create_second_path_first_task(x, frame_questions, widgets_frame_question, answers_stud_entry))
    option_menu_answer.config(width=25, font=("Gabriola", "14"))
    option_menu_answer.place(x=425, y=0)
    widgets.append(option_menu_answer)

    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1, font=("Arial", "12", "italic"), background="white",
                             cursor="hand2", command=lambda : check_first_task(dict_rule, answers_stud_entry, variable, option_menu_answer, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_post, text="Повторить", width=15, height=1, font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2", command=lambda: restart_first_task(variable, option_menu_answer, dict_rule, label_rule, widgets_frame_question, answers_stud_entry, label_true_tasks))
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


def create_second_path_first_task(variable, frame, widgets_frame_question, answers_stud_entry):

    for elem in widgets_frame_question:
        elem.destroy()

    for i in range(len(answers_stud_entry)):
        answers_stud_entry.pop()

    if variable == 'проверяет наличие пометки':
        label_question_one = Tk.Label(master=frame, width=100,
                                  text="Если текущая ячейка пустая, то необходимо осуществить переход на ",
                                  font=("Gabriola", "20"), background="white")
        label_question_one.place(x=0, y=60)
        widgets_frame_question.append(label_question_one)

        entry_answer_one = Tk.Entry(master=frame, width=10, font=('Arial', 16, 'bold'), relief="raised")
        entry_answer_one.place(x=500, y=100)
        widgets_frame_question.append(entry_answer_one)
        answers_stud_entry.append(entry_answer_one)

        label_question_two = Tk.Label(master=frame, width=100,
                                      text="Иначе если текущая ячейка непустая, то необходимо осуществить переход на ",
                                      font=("Gabriola", "20"), background="white")
        label_question_two.place(x=0, y=130)
        widgets_frame_question.append(label_question_two)

        entry_answer_two = Tk.Entry(master=frame, width=10, font=('Arial', 16, 'bold'), relief="raised")
        entry_answer_two.place(x=500, y=170)
        widgets_frame_question.append(entry_answer_two)
        answers_stud_entry.append(entry_answer_two)

    elif variable != 'останавливает программу':
        label_question = Tk.Label(master=frame, width=50, justify="left",
                                        text="На какую строку осуществляется переход?",
                                        font=("Gabriola", "20"), background="white")
        label_question.place(x=0, y=60)
        widgets_frame_question.append(label_question)

        entry_answer = Tk.Entry(master=frame, width=10, font=('Arial', 16, 'bold'), relief="raised")
        entry_answer.place(x=500, y=70)
        widgets_frame_question.append(entry_answer)
        answers_stud_entry.append(entry_answer)


def check_first_task(dict_rule, answers_stud_entry, variable, option_menu_answer, label_true_tasks):

    if variable.get() == "выберите вариант ответа":
        return messagebox.showerror(title="Ошибка", message="Похоже ты забыл выбрать вариант ответа..", parent=option_menu_answer)

    for entry in answers_stud_entry:
        if entry.get() == '':
            return messagebox.showerror(title="Ошибка", message="Похоже ты забыл написать ответ..", parent=option_menu_answer)

    dict_commands = {'<': 'передвигает каретку влево', '>': 'передвигает каретку вправо', '1': 'ставит пометку', '0': 'стирает пометку',
                    '?': 'проверяет наличие пометки', '.': 'останавливает программу'}

    list_rule = dict_rule['rule'].split()
    count_true = 0
    if variable.get() == dict_commands[list_rule[0]]:
        option_menu_answer.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
        count_true += 1
        flag = True
    else:
        option_menu_answer.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
        flag = False

    if flag:
        for i, entry in enumerate(answers_stud_entry):
            if entry.get() == list_rule[i+1].strip(','):
                entry.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
                count_true += 1
            else:
                entry.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
    else:
        for i, entry in enumerate(answers_stud_entry):
            if i != 0:
                answers_stud_entry[i].config(highlightthickness=2, highlightbackground="red", highlightcolor="red")
            if i == 0 and entry.get() == list_rule[i+1].strip(','):
                entry.config(highlightthickness=2, highlightbackground="green", highlightcolor="green")
            else:
                entry.config(highlightthickness=2, highlightbackground="red", highlightcolor="red")

    if count_true == len(list_rule):
        label_true_tasks.config(text="Молодец! Ты верно выполнил задание!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуй ещё раз!")


def restart_first_task(variable,option_menu_answer, dict_rule, label_rule, widgets_frame_question, answers_stud_entry, label_true_tasks):
    variable.set('выберите вариант ответа')
    dict_rule['rule'] = create_random_rule_for_double_digit()
    label_rule["text"] = dict_rule['rule']
    option_menu_answer.config(highlightbackground="white", highlightcolor="white")

    for widget in widgets_frame_question:
        widget.destroy()

    for i in range(len(answers_stud_entry)):
        answers_stud_entry.pop()

    label_true_tasks.config(text="")


def second_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_post = dict_windows["window_learning_post"]

    label_number_task = Tk.Label(master=window_learning_post, width=80, text="Задание 2", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_post, width=100, text=SECOND_TASK,
                                      justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    dict_rule = {'rule': create_random_rule_for_double_digit()}

    label_task = Tk.Label(master=window_learning_post, width=100, text=create_text_second_task(dict_rule), justify="left", font=("Gabriola", "18"),
                                background="white")
    label_task.place(x=50, y=200)
    widgets.append(label_task)
    entry_answer = Tk.Entry(master=window_learning_post, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer.place(x=350, y=350)
    widgets.append(entry_answer)

    label_true_tasks = Tk.Label(master=window_learning_post, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_second_task(dict_rule, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_post, text="Повторить", width=15, height=1,
                               font=("Arial", "12", "italic"), background="white",
                               cursor="hand2",
                               command=lambda: restart_second_task(dict_rule, entry_answer, label_task, label_true_tasks))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_post)
    label_next = Tk.Label(window_learning_post, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_post, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2", command=lambda: fourth_task_learn(dict_windows, widgets))
    button_next.place(x=950, y=705)
    widgets.append(button_next)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_post)
    label_previos = Tk.Label(window_learning_post, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_post, text="Предыдущее задание  ", image=photo_previos,
                            compound="left", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2", command=lambda: first_task_learn(dict_windows, widgets))
    button_previos.place(x=150, y=705)
    widgets.append(button_previos)


def create_text_second_task(dict_rule):
    list_rule = dict_rule['rule'].split()

    if len(list_rule) == 3:
       return f'Если метка стоит, то переходим на строку {list_rule[1].strip(",")}, иначе переходим на строку {list_rule[2]}'
    elif list_rule[0] == '0':
        transition = f'Стираем метку, '
    elif list_rule[0] == '1':
        transition = f'Ставим метку, '
    elif list_rule[0] == '<':
        transition = f'Сдвигаем карутку влево, '
    elif list_rule[0] == '>':
        transition = f'Сдвигаем карутку вправо, '
    else:
        return f'Останавливаем программу'
    return transition + f'переходим на строку {list_rule[1]}'


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

    dict_rule['rule'] = create_random_rule_for_double_digit()
    label_task.config(text=create_text_second_task(dict_rule))


def third_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_post = dict_windows["window_learning_post"]

    label_number_task = Tk.Label(master=window_learning_post, width=80, text="Задание 3", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat", command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_post, width=100,
                                      justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    label_true_tasks = Tk.Label(master=window_learning_post, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=100, y=600)
    widgets.append(label_true_tasks)

    label_answer = Tk.Label(master=window_learning_post, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    frame_answer = Tk.Frame(master=window_learning_post, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer.place(x=1, y=1)
    widgets.append(entry_answer)

    list_true_answer = []

    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_third_task(list_true_answer, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_post, text="Повторить", width=15, height=1,
                               font=("Arial", "12", "italic"), background="white",
                               cursor="hand2",
                               command=lambda: restart_third_task(label_description_task, list_true_answer, label_true_tasks, entry_answer, turing_alg_obj, turing_alg_wid))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_post)
    label_next = Tk.Label(window_learning_post, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_post, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2", command=lambda: fourth_task_learn(dict_windows, widgets))
    button_next.place(x=950, y=705)
    widgets.append(button_next)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_post)
    label_previos = Tk.Label(window_learning_post, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_post, text="Предыдущее задание  ", image=photo_previos,
                               compound="left", width=200, height=25, font=("Arial", "12", "italic"),
                               background="white",
                               cursor="hand2", command=lambda: second_task_learn(dict_windows, widgets))
    button_previos.place(x=150, y=705)
    widgets.append(button_previos)


def fourth_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_post = dict_windows["window_learning_post"]

    label_number_task = Tk.Label(master=window_learning_post, width=80, text="Задание 3", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat",
                            command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_post, width=100,
                                      justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    label_true_tasks = Tk.Label(master=window_learning_post, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=550, y=600)
    widgets.append(label_true_tasks)

    frame_answer = Tk.Frame(master=window_learning_post, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer.place(x=1, y=1)
    widgets.append(entry_answer)

    list_true_answer = []
    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_fourth_task(list_true_answer, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    text_task_condition = Tk.Text(master=window_learning_post, width=131, height=8, font=("Times New Roman", "14"))
    text_task_condition.place(x=10, y=90)
    widgets.append(text_task_condition)

    frame_table_rules = Tk.Frame(master=window_learning_post, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=70, y=400)
    widgets.append(frame_table_rules)

    frame_infinity_tape = Tk.Frame(master=window_learning_post, width=1140, height=100, padx=0, pady=0)
    frame_infinity_tape.place(x=30, y=275)
    widgets.append(frame_infinity_tape)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_learning_post)
    label_point = Tk.Label(window_learning_post, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40, background="white")
    label_point.place(x=547, y=0)

    label_answer = Tk.Label(master=window_learning_post, text="Ваш ответ:", justify="center", font=("Gabriola", "24"),
                            background="white")
    label_answer.place(x=900, y=425)
    widgets.append(label_answer)

    frame_answer = Tk.Frame(master=window_learning_post, width=265, height=50, background=rgb_hack((1, 116, 64)),
                            border=10)
    frame_answer.place(x=900, y=500)
    widgets.append(frame_answer)
    entry_answer_stud = Tk.Entry(master=frame_answer, width=20, font=('Arial', 16, 'bold'), relief="raised")
    entry_answer_stud.place(x=1, y=1)
    widgets.append(entry_answer_stud)

    list_true_answer = []

    button_right = Tk.Button(master=window_learning_post, width=1, height=6,
                             command=lambda: movement_right(post_alg_obj, post_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)
    widgets.append(button_right)

    button_left = Tk.Button(master=window_learning_post, width=1, height=6,
                            command=lambda: movement_left(post_alg_obj, post_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)
    widgets.append(button_left)

    table_rules = [[] for i in range(9)]
    alphabetical = []
    alphabet_size = 2
    infinity_tape = {}
    output_elm_ids = [-9, 9]
    post_alg_obj = PostAlg(table_rules, alphabetical, 0, alphabet_size)
    post_alg_wid = ObjPostAlg(infinity_tape, frame_infinity_tape, output_elm_ids, text_task_condition,
                              frame_table_rules, button_right, button_left)

    read_and_create_task(post_alg_obj, post_alg_wid, 4, list_true_answer)
    
    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_fourth_task(list_true_answer, entry_answer_stud, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_post, text="Повторить", width=15, height=1,
                               font=("Arial", "12", "italic"), background="white",
                               cursor="hand2",
                               command=lambda: restart_fourth_task(label_description_task, list_true_answer,
                                                                   label_true_tasks, entry_answer, post_alg_obj,
                                                                   post_alg_wid))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_next = Image.open(Path.cwd() / "Image" / "Step.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_learning_post)
    label_next = Tk.Label(window_learning_post, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_learning_post, text="Следующее задание  ", image=photo_next,
                            compound="right", width=200, height=25, font=("Arial", "12", "italic"), background="white",
                            cursor="hand2", command=lambda: fifth_task_learn(dict_windows, widgets))
    button_next.place(x=950, y=705)
    widgets.append(button_next)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_post)
    label_previos = Tk.Label(window_learning_post, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_post, text="Предыдущее задание  ", image=photo_previos,
                               compound="left", width=200, height=25, font=("Arial", "12", "italic"),
                               background="white",
                               cursor="hand2", command=lambda: second_task_learn(dict_windows, widgets))
    button_previos.place(x=150, y=705)
    widgets.append(button_previos)


def restart_fourth_task(label_description_task, list_true_answer, label_true_tasks, entry_answer, post_alg_obj, post_alg_wid):
    cleaning_widgets(post_alg_obj, post_alg_wid)
    label_true_tasks.config(text="")
    entry_answer.delete("0", "end")
    list_true_answer.clear()
    read_and_create_task(post_alg_obj, post_alg_wid, 4, list_true_answer)


def check_fourth_task(list_true_answer, entry_answer, label_true_tasks):
    if entry_answer.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже ты забыл написать ответ..", parent=entry_answer)
    if list_true_answer[0] == entry_answer.get():
        label_true_tasks.config(text="Молодец! Ты верно выполнил задание!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуй ещё раз!")


def fifth_task_learn(dict_windows, widgets):
    widgets = destroy_widgets(widgets)
    window_learning_post = dict_windows["window_learning_post"]

    label_number_task = Tk.Label(master=window_learning_post, width=80, text="Задание 4", justify="center",
                                 font=("Gabriola", "28"), background="white")
    label_number_task.place(x=0, y=10)
    widgets.append(label_number_task)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_learning_post)
    label_exit = Tk.Label(window_learning_post, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_learning_post, image=photo_exit, width=40, height=40, cursor="hand2",
                            background="white", justify="center", relief="flat",
                            command=lambda: return_window_for_algorithms(dict_windows))
    button_exit.place(x=5, y=705)
    widgets.append(button_exit)

    label_description_task = Tk.Label(master=window_learning_post, width=100,
                                      justify="center", font=("Gabriola", "20"), background="white")
    label_description_task.place(x=20, y=100)
    widgets.append(label_description_task)

    label_true_tasks = Tk.Label(master=window_learning_post, width=50, justify="left", font=("Gabriola", "20"),
                                background="white")
    label_true_tasks.place(x=550, y=600)
    widgets.append(label_true_tasks)

    list_true_answer = []
    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_fourth_task(list_true_answer, entry_answer, label_true_tasks))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    text_task_condition = Tk.Text(master=window_learning_post, width=131, height=8, font=("Times New Roman", "14"))
    text_task_condition.place(x=10, y=90)
    widgets.append(text_task_condition)

    frame_table_rules = Tk.Frame(master=window_learning_post, width=800, height=250, border=10,
                                 background=rgb_hack((1, 116, 64)))
    frame_table_rules.place(x=70, y=400)
    widgets.append(frame_table_rules)

    frame_infinity_tape = Tk.Frame(master=window_learning_post, width=1140, height=100, padx=0, pady=0)
    frame_infinity_tape.place(x=30, y=275)
    widgets.append(frame_infinity_tape)

    img_point = Image.open(Path.cwd() / "Image" / "pointer.png")
    photo_point = ImageTk.PhotoImage(img_point, master=window_learning_post)
    label_point = Tk.Label(window_learning_post, image=photo_point)
    label_point.image = photo_point
    label_point = Tk.Label(master=frame_infinity_tape, image=photo_point, width=40, height=40, background="white")
    label_point.place(x=547, y=0)

    list_true_answer = []

    button_right = Tk.Button(master=window_learning_post, width=1, height=6,
                             command=lambda: movement_right(post_alg_obj, post_alg_wid))
    button_right.place(x=1170, y=275, height=100, width=30)
    widgets.append(button_right)

    button_left = Tk.Button(master=window_learning_post, width=1, height=6,
                            command=lambda: movement_left(post_alg_obj, post_alg_wid))
    button_left.place(x=0, y=275, height=100, width=30)
    widgets.append(button_left)

    entry_answer_stud = Tk.Entry(master=window_learning_post, width=20, font=('Arial', 16, 'bold'), relief="raised")
    widgets.append(entry_answer_stud)

    table_rules = [[] for i in range(9)]
    alphabetical = []
    alphabet_size = 2
    infinity_tape = {}
    output_elm_ids = [-9, 9]
    post_alg_obj = PostAlg(table_rules, alphabetical, 0, alphabet_size)
    post_alg_wid = ObjPostAlg(infinity_tape, frame_infinity_tape, output_elm_ids, text_task_condition,
                              frame_table_rules, button_right, button_left)

    read_and_create_task(post_alg_obj, post_alg_wid, 5, list_true_answer)

    button_verification = Tk.Button(master=window_learning_post, text="Проверить", width=15, height=1,
                                    font=("Arial", "12", "italic"), background="white",
                                    cursor="hand2",
                                    command=lambda: check_fifth_task(list_true_answer, label_true_tasks, post_alg_wid))
    button_verification.place(x=650, y=705)
    widgets.append(button_verification)

    button_restart = Tk.Button(master=window_learning_post, text="Повторить", width=15, height=1,
                               font=("Arial", "12", "italic"), background="white",
                               cursor="hand2",
                               command=lambda: restart_fifth_task(label_description_task, list_true_answer, label_true_tasks, post_alg_obj, post_alg_wid))
    button_restart.place(x=450, y=705)
    widgets.append(button_restart)

    img_previos = Image.open(Path.cwd() / "Image" / "Step_previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_learning_post)
    label_previos = Tk.Label(window_learning_post, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_learning_post, text="Предыдущее задание  ", image=photo_previos,
                               compound="left", width=200, height=25, font=("Arial", "12", "italic"),
                               background="white",
                               cursor="hand2", command=lambda: fourth_task_learn(dict_windows, widgets))
    button_previos.place(x=150, y=705)
    widgets.append(button_previos)


def check_fifth_task(list_true_answer, label_true_tasks, post_alg_wid):
    if post_alg_wid.entry_answer_stud_third.get() == "":
        return messagebox.showerror(title="Ошибка", message="Похоже ты забыл написать ответ..",
                                    parent=post_alg_wid.entry_answer_stud_third)
    if list_true_answer[0] == post_alg_wid.entry_answer_stud_third.get():
        label_true_tasks.config(text="Молодец! Ты верно выполнил задание!")
    else:
        label_true_tasks.config(text="Увы.. Допущена ошибка.. Попробуй ещё раз!")


def restart_fifth_task(label_description_task, list_true_answer, label_true_tasks, post_alg_obj, post_alg_wid):
    cleaning_widgets(post_alg_obj, post_alg_wid)
    label_true_tasks.config(text="")
    list_true_answer.clear()
    read_and_create_task(post_alg_obj, post_alg_wid, 5, list_true_answer)


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
        post_alg_wid.infinity_tape[ind].option_menu.place(x=place_x, y=62, width=60, height=40)

        post_alg_wid.list_label_ind[i]["text"] = str(ind)
        i += 1

        place_x += 60


def changing_alphabet(post_alg_obj, post_alg_wid, var, need_cleaning=True):
    post_alg_obj.alphabetical = []
    post_alg_obj.alphabet_size = var
    if post_alg_obj.alphabet_size == 2:
        post_alg_obj.alphabetical = [" ", u'\u2714']
    elif post_alg_obj.alphabet_size == 3:
        post_alg_obj.alphabetical = [" ", "0", "1"]

    cleaning_widgets(post_alg_obj, post_alg_wid)

    creating_rules_table(post_alg_obj, post_alg_wid)


def delete_option_menu_from_frame(frame: Tk.Frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tkinter.OptionMenu):
            widget.place(x=-1000, y=-1000)


def delete_table_rules(post_alg_obj):
    for elem in post_alg_obj.list_number_row:
        cell = elem
        cell.destroy()
    post_alg_obj.list_number_row.clear()

    for elem in post_alg_obj.list_entry_heading:
        cell = elem
        cell.destroy()
    post_alg_obj.list_entry_heading.clear()

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

    post_alg_obj.table_rules = [[] for i in range(9)]

    post_alg_wid.output_elm_ids = [-9, 9]

    delete_option_menu_from_frame(post_alg_wid.frame_infinity_tape)


def creating_rules_table(post_alg_obj, post_alg_wid):
    list_heading = ['Команда', 'Переход']
    for i in range(len(post_alg_obj.table_rules) + 1):  # создание таблицы правил
        for j in range(3):
            cell = Tk.Entry(master=post_alg_wid.frame_table_rules, width=16, font=('Arial', 16, 'bold'),
                            relief="raised", justify='center')
            if j == 0 and i > 0:
                cell.insert("end", i)
                cell["state"] = "disabled"
                cell["width"] = 3
                post_alg_obj.list_number_row.append(cell)
            elif i == 0 and j > 0:
                cell.insert("end", list_heading[j - 1])
                cell["state"] = "disabled"
                post_alg_obj.list_entry_heading.append(cell)
            elif i == 0 and j == 0:
                cell["state"] = "disabled"
                cell["width"] = 3
                post_alg_obj.list_entry_heading.append(cell)
            elif i > 0 and j > 0:
                post_alg_obj.table_rules[i - 1].append(cell)
            cell.grid(row=i, column=j)


def fill_rules_table(post_alg_obj, rules_table):
    for i in range(0, len(post_alg_obj.table_rules)):

        current_rules_list = rules_table.get(str(i))

        if current_rules_list:
            for index, cell in enumerate(post_alg_obj.table_rules[i]):
                cell.insert("end", current_rules_list[index])


def creating_and_fill_infinity_tape(post_alg_obj, post_alg_wid, expression_info, pointer_index):
    place_x = 0
    post_alg_obj.pointer_index = pointer_index

    min_ind, max_ind = min(expression_info.keys()), max(expression_info.keys())
    min_ind, max_ind = min([int(min_ind), pointer_index - 9]), max([int(max_ind), pointer_index + 10])

    post_alg_wid.output_elm_ids = [pointer_index - 9, pointer_index + 10]

    for ind in range(min_ind, max_ind + 1):
        symbol = Tk.StringVar(post_alg_wid.frame_infinity_tape)
        symbol.set(expression_info.get(str(ind), " "))

        current_opt_menu = Tk.OptionMenu(post_alg_wid.frame_infinity_tape, symbol, *post_alg_obj.alphabetical)
        current_opt_menu.config(width=2, height=2, font=('Helvetica', 12))
        current_my_opt_menu = MyOptionMenu(current_opt_menu, symbol, post_alg_obj.alphabetical)
        post_alg_wid.infinity_tape[ind] = current_my_opt_menu

        lbl = Tk.Label(master=post_alg_wid.frame_infinity_tape, text=str(ind), justify="left", font=("Verdana", "12"))

        if post_alg_wid.output_elm_ids[0] <= ind <= post_alg_wid.output_elm_ids[1]:
            current_opt_menu.place(x=place_x, y=63, width=60, height=40)
            lbl.place(x=place_x + 20, y=44)
            place_x += 60
            post_alg_wid.list_label_ind.append(lbl)


def read_and_create_task(post_alg_obj, post_alg_wid, number_task, list_true_answer, entry_answer_stud=None):
    with open("LEARNING_POST.json", encoding='utf-8') as f:
        example_info = json.load(f)

    list_tasks = []
    for dct in example_info:
        if dct["type"] == number_task:
            list_tasks.append(dct)

    number_option = randint(0, 2)
    current_tasks = list_tasks[number_option]

    counter_command = current_tasks.get("counter_command")
    pointer_index = current_tasks.get("pointer_index")
    table_rules = current_tasks.get("table_rules")
    expression_info = current_tasks.get("expression")
    task_condition = current_tasks.get("task_condition")
    alphabetical_size = current_tasks.get("alphabetical_size")
    list_true_answer.append(current_tasks.get("answer"))

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

    for lst in post_alg_obj.table_rules:
        for elem in lst:
            elem["state"] = "disabled"

    if number_task == 5:
        num_row = current_tasks.get("num_cell_row")
        num_col = current_tasks.get("num_cell_col")
        cell = post_alg_obj.table_rules[num_row][num_col]
        cell["state"] = "normal"
        post_alg_wid.entry_answer_stud_third = cell
        cell["relief"] = "sunken"

    # if number_task == 4:
    #     post_alg_wid.lst_var = current_tasks.get("var")

    post_alg_wid.list_true_answer.append(current_tasks.get("answer"))