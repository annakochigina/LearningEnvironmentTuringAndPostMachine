import tkinter as Tk
from PIL import Image, ImageTk
import const.text as text
from processor import turing_machine, post_machine, control_turing, control_post, learning_turing
from pathlib import Path
import os

BRIEF_REFERENCE_TURING = text.CONST_BRIEF_REFERENCE_TURING
BRIEF_REFERENCE_TURING_TWO = text.CONST_BRIEF_REFERENCE_TURING_TWO
DESCRIPTION_ALGORITHM_TURING_ONE = text.CONST_DESCRIPTION_ALGORITHM_TURING_ONE
DESCRIPTION_ALGORITHM_TURING_TWO = text.CONST_DESCRIPTION_ALGORITHM_TURING_TWO

BRIEF_REFERENCE_POST = text.CONST_BRIEF_REFERENCE_POST
BRIEF_REFERENCE_POST_TWO = text.CONST_BRIEF_REFERENCE_POST_TWO
DESCRIPTION_ALGORITHM_POST_ONE = text.CONST_DESCRIPTION_ALGORITHM_POST_ONE
DESCRIPTION_ALGORITHM_POST_TWO = text.CONST_DESCRIPTION_ALGORITHM_POST_TWO


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def return_first_form(dict_windows):
    dict_windows["window_for_algorithms"].destroy()
    dict_windows["first_window"].deiconify()


def menu_for_algorithms(dict_windows):
    # создание окна
    window_for_algorithms = Tk.Tk()
    window_for_algorithms_width_center = (window_for_algorithms.winfo_screenwidth()) // 2 - 600
    window_for_algorithms_height_center = (window_for_algorithms.winfo_screenheight()) // 2 - 375
    window_for_algorithms.geometry(
        "1200x750+{}+{}".format(window_for_algorithms_width_center, window_for_algorithms_height_center))
    window_for_algorithms.resizable(width=False, height=False)
    # window_for_algorithms.config(bg=rgb_hack((1, 116, 64)))
    dict_windows["window_for_algorithms"] = window_for_algorithms
    return window_for_algorithms, dict_windows


def destroy_objects(objects):
    for obj in objects:
        obj.destroy()
    return []


def first_page_theory(window_for_algorithms, objects, widgets_theory):
    destroy_objects(widgets_theory)

    frame_text_theory = Tk.Frame(master=window_for_algorithms, border=10, width=1200, height=705,
                                 background=rgb_hack((1, 116, 64)))
    frame_text_theory.place(x=0, y=0)
    objects.append(frame_text_theory)
    widgets_theory.append(frame_text_theory)

    text_turing = Tk.Label(master=frame_text_theory, justify="left", width=96, height=26,
                           font=("Bahnschrift Light", "16"), background="white")
    text_turing.place(x=10, y=10)
    objects.append(text_turing)
    widgets_theory.append(text_turing)

    label_info_one = Tk.Label(master=text_turing, text=BRIEF_REFERENCE_TURING, justify="left",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_one.place(x=5, y=52)
    objects.append(label_info_one)
    widgets_theory.append(label_info_one)

    label_info_two = Tk.Label(master=text_turing, text=BRIEF_REFERENCE_TURING_TWO, justify="right",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_two.place(x=375, y=390)
    objects.append(label_info_two)
    widgets_theory.append(label_info_two)

    label_turing = Tk.Label(master=text_turing, text="Машина Тьюринга", justify="center", width=40, height=1,
                            font=("Bahnschrift Light", "24", "bold"), background="white")
    label_turing.place(x=0, y=5)
    objects.append(label_turing)
    widgets_theory.append(label_turing)

    img_tur = Image.open(Path.cwd() / "Image" / "turing.png")
    photo_tur = ImageTk.PhotoImage(img_tur, master=text_turing)
    label_tur = Tk.Label(text_turing, image=photo_tur)
    label_tur.image = photo_tur
    label_tur.place(x=810, y=10)
    widgets_theory.append(label_tur)

    img_mach_tur = Image.open(Path.cwd() / "Image" / "machine_turing.png")
    photo_mach_tur = ImageTk.PhotoImage(img_mach_tur, master=text_turing)
    label_mach_tur = Tk.Label(text_turing, image=photo_mach_tur)
    label_mach_tur.image = photo_mach_tur
    label_mach_tur.place(x=10, y=390)
    widgets_theory.append(label_mach_tur)

    img_next = Image.open(Path.cwd() / "Image" / "next.png")
    photo_next = ImageTk.PhotoImage(img_next, master=window_for_algorithms)
    label_next = Tk.Label(window_for_algorithms, image=photo_next)
    label_next.image = photo_next
    button_next = Tk.Button(master=window_for_algorithms, image=photo_next, width=40, height=40, background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: second_page_theory(window_for_algorithms, objects, widgets_theory))
    button_next.place(x=1150, y=705)
    widgets_theory.append(button_next)
    objects.append(button_next)


def second_page_theory(window_for_algorithms, objects, widgets_theory):
    destroy_objects(widgets_theory)

    frame_text_theory = Tk.Frame(master=window_for_algorithms, border=10, width=1200, height=705,
                                 background=rgb_hack((1, 116, 64)))
    frame_text_theory.place(x=0, y=0)
    objects.append(frame_text_theory)
    widgets_theory.append(frame_text_theory)

    text_turing = Tk.Label(master=frame_text_theory, justify="left", width=96, height=26,
                           font=("Bahnschrift Light", "16"), background="white")
    text_turing.place(x=10, y=10)
    objects.append(text_turing)
    widgets_theory.append(text_turing)

    label_turing = Tk.Label(master=text_turing, text="Что собой представляет машина Тьюринга?", justify="center",
                            width=40, height=1, font=("Bahnschrift Light", "24", "bold"), background="white")
    label_turing.place(x=0, y=5)
    objects.append(label_turing)
    widgets_theory.append(label_turing)

    label_info_one = Tk.Label(master=text_turing, text=DESCRIPTION_ALGORITHM_TURING_ONE, justify="left",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_one.place(x=5, y=52)
    objects.append(label_info_one)
    widgets_theory.append(label_info_one)

    img_tape = Image.open(Path.cwd() / "Image" / "tape.png")
    photo_tape = ImageTk.PhotoImage(img_tape, master=text_turing)
    label_tape = Tk.Label(text_turing, image=photo_tape)
    label_tape.image = photo_tape
    label_tape.place(x=400, y=110)
    widgets_theory.append(label_tape)

    label_info_two = Tk.Label(master=text_turing, text=DESCRIPTION_ALGORITHM_TURING_TWO, justify="left",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_two.place(x=5, y=230)
    objects.append(label_info_two)
    widgets_theory.append(label_info_two)

    img_tappe = Image.open(Path.cwd() / "Image" / "tappe.png")
    photo_tappe = ImageTk.PhotoImage(img_tappe, master=text_turing)
    label_tappe = Tk.Label(text_turing, image=photo_tappe)
    label_tappe.image = photo_tappe
    label_tappe.place(x=10, y=400)
    widgets_theory.append(label_tappe)

    img_table = Image.open(Path.cwd() / "Image" / "table.png")
    photo_table = ImageTk.PhotoImage(img_table, master=text_turing)
    label_table = Tk.Label(text_turing, image=photo_table)
    label_table.image = photo_table
    label_table.place(x=400, y=510)
    widgets_theory.append(label_table)

    img_previos = Image.open(Path.cwd() / "Image" / "previos.png")
    photo_previos = ImageTk.PhotoImage(img_previos, master=window_for_algorithms)
    label_previos = Tk.Label(window_for_algorithms, image=photo_previos)
    label_previos.image = photo_previos
    button_previos = Tk.Button(master=window_for_algorithms, image=photo_previos, width=40, height=40, background="white",
                            relief="flat", cursor="hand2",
                            command=lambda: first_page_theory(window_for_algorithms, objects, widgets_theory))
    button_previos.place(x=55, y=705)
    widgets_theory.append(button_previos)


def theory_turing(objects, dict_windows):
    destroy_objects(objects)
    window_for_algorithms = dict_windows["window_for_algorithms"]
    widgets_theory = []
    first_page_theory(window_for_algorithms, objects, widgets_theory)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_for_algorithms)
    label_exit = Tk.Label(window_for_algorithms, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_for_algorithms, image=photo_exit, width=40, height=40, background="white",
                            relief="flat", cursor="hand2", command=lambda: menu_turing(objects, dict_windows))
    button_exit.place(x=5, y=705)
    objects.append(button_exit)


def create_menu_for_algorithms_turing(dict_windows):
    window_for_algorithms, dict_windows = menu_for_algorithms(dict_windows)
    objects = []
    menu_turing(objects, dict_windows)


def create_window_machine_turing(dict_windows):
    dict_windows["window_for_algorithms"].withdraw()
    window_machine_turing = turing_machine.create_machine_turing(dict_windows)


def create_window_learning_turing(dict_windows):
    dict_windows["window_for_algorithms"].withdraw()
    window_learning_turing = learning_turing.create_learning_turing(dict_windows)


def create_window_turing_control(dict_windows):
    dict_windows["window_for_algorithms"].withdraw()
    window_control_turing = control_turing.create_control_turing(dict_windows)


def menu_turing(objects, dict_windows):  # меню для работы с машиной Тьюринга

    window_for_algorithms = dict_windows.get("window_for_algorithms")
    objects = destroy_objects(objects)

    window_for_algorithms.title("Машина Тьюринга")
    # создание title
    img_fon = Image.open(Path.cwd() / "Image" / "Фон2.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_for_algorithms)
    label_fon = Tk.Label(window_for_algorithms, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_for_algorithms, width=1200, height=375)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)
    objects.append(canvas)

    frame_button = Tk.Frame(master=window_for_algorithms, width=1200, height=375, background="white")
    frame_button.place(x=0, y=375)
    objects.append(frame_button)

    label_title = Tk.Label(master=window_for_algorithms, text="Машина Тьюринга", justify="left", width="25", height=1,
                           font=("Gabriola", "48", "bold"), background=rgb_hack((1, 116, 64)))
    label_title.pack(pady=(300, 200))
    objects.append(label_title)

    # создание кнопок для работы с машиной Тьюринга
    img_theory = Image.open(Path.cwd() / "Image" / "theory.png")
    photo_theory = ImageTk.PhotoImage(img_theory, master=window_for_algorithms)
    label_theory = Tk.Label(window_for_algorithms, image=photo_theory)
    label_theory.image = photo_theory
    button_theory = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_theory, width=200, height=200,
                              cursor="hand2", command=lambda: theory_turing(objects, dict_windows))
    button_theory.place(x=125, y=450)
    objects.append(button_theory)

    img_training = Image.open(Path.cwd() / "Image" / "training.png")
    photo_training = ImageTk.PhotoImage(img_training, master=window_for_algorithms)
    label_training = Tk.Label(window_for_algorithms, image=photo_theory)
    label_training.image = photo_training
    button_training = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_training, width=200, height=200,
                              cursor="hand2", command=lambda: create_window_learning_turing(dict_windows))
    button_training.place(x=375, y=450)
    objects.append(button_training)

    img_trainer = Image.open(Path.cwd() / "Image" / "trainer.png")
    photo_trainer = ImageTk.PhotoImage(img_trainer, master=window_for_algorithms)
    label_trainer = Tk.Label(window_for_algorithms, image=photo_trainer)
    label_trainer.image = photo_trainer
    button_trainer = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_trainer, width=200, height=200,
                               cursor="hand2", command=lambda: create_window_machine_turing(dict_windows))
    button_trainer.place(x=625, y=450)
    objects.append(button_trainer)

    img_control = Image.open(Path.cwd() / "Image" / "control.png")
    photo_control = ImageTk.PhotoImage(img_control, master=window_for_algorithms)
    label_control = Tk.Label(window_for_algorithms, image=photo_control)
    label_control.image = photo_control
    button_control = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_control, width=200, height=200,
                               cursor="hand2", command=lambda: create_window_turing_control(dict_windows))
    button_control.place(x=875, y=450)
    objects.append(button_control)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_for_algorithms)
    label_exit = Tk.Label(window_for_algorithms, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_exit, width=40, height=30,
                            cursor="hand2", background="white", command=lambda: return_first_form(dict_windows))
    button_exit.place(x=5, y=710)
    objects.append(button_exit)

    window_for_algorithms.protocol("WM_DELETE_WINDOW", lambda: return_first_form(dict_windows))


def create_window_machine_post(dict_windows):
    dict_windows["window_for_algorithms"].withdraw()
    window_machine_postg = post_machine.create_machine_post(dict_windows)


def brief_reference_post(objects, dict_windows):
    destroy_objects(objects)
    window_for_algorithms = dict_windows["window_for_algorithms"]

    frame_text_theory = Tk.Frame(master=window_for_algorithms, border=10, width=1200, height=705,
                                 background=rgb_hack((1, 116, 64)))
    frame_text_theory.place(x=0, y=0)
    objects.append(frame_text_theory)

    text_post = Tk.Label(master=frame_text_theory, justify="left", width=96, height=26,
                         font=("Bahnschrift Light", "16"), background="white")
    text_post.place(x=10, y=10)
    objects.append(text_post)

    label_turing = Tk.Label(master=text_post, text="Машина Поста", justify="center", width=40, height=1,
                            font=("Bahnschrift Light", "24", "bold"), background="white")
    label_turing.place(x=0, y=5)
    objects.append(label_turing)

    label_info_one = Tk.Label(master=text_post, text=BRIEF_REFERENCE_POST, justify="left",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_one.place(x=5, y=52)
    objects.append(label_info_one)

    img_post = Image.open(Path.cwd() / "Image" / "post.png")
    photo_post = ImageTk.PhotoImage(img_post, master=text_post)
    label_post = Tk.Label(text_post, image=photo_post)
    label_post.image = photo_post
    label_post.place(x=810, y=10)

    img_mach_post = Image.open(Path.cwd() / "Image" / "machine_post.png")
    photo_mach_post = ImageTk.PhotoImage(img_mach_post, master=text_post)
    label_mach_post = Tk.Label(text_post, image=photo_mach_post)
    label_mach_post.image = photo_mach_post
    label_mach_post.place(x=10, y=390)

    label_info_two = Tk.Label(master=text_post, text=BRIEF_REFERENCE_POST_TWO, justify="right",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_two.place(x=375, y=390)
    objects.append(label_info_two)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_for_algorithms)
    label_exit = Tk.Label(window_for_algorithms, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_for_algorithms, image=photo_exit, width=40, height=40, background="white",
                            relief="flat", cursor="hand2", command=lambda: menu_post(objects, dict_windows))
    button_exit.place(x=5, y=705)
    objects.append(button_exit)


def description_algorithm_post(objects, dict_windows):
    destroy_objects(objects)
    window_for_algorithms = dict_windows["window_for_algorithms"]

    frame_text_theory = Tk.Frame(master=window_for_algorithms, border=10, width=1200, height=705,
                                 background=rgb_hack((1, 116, 64)))
    frame_text_theory.place(x=0, y=0)
    objects.append(frame_text_theory)

    text_post = Tk.Label(master=frame_text_theory, justify="left", width=96, height=26,
                         font=("Bahnschrift Light", "16"), background="white")
    text_post.place(x=10, y=10)
    objects.append(text_post)

    label_post = Tk.Label(master=text_post, text="Что собой представляет машина Поста?", justify="center", width=40,
                          height=1, font=("Bahnschrift Light", "24", "bold"), background="white")
    label_post.place(x=0, y=5)
    objects.append(label_post)

    label_info_one = Tk.Label(master=text_post, text=DESCRIPTION_ALGORITHM_POST_ONE, justify="left",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_one.place(x=5, y=50)
    objects.append(label_info_one)

    img_tapep = Image.open(Path.cwd() / "Image" / "tapep.png")
    photo_tapep = ImageTk.PhotoImage(img_tapep, master=text_post)
    label_tapep = Tk.Label(text_post, image=photo_tapep)
    label_tapep.image = photo_tapep
    label_tapep.place(x=10, y=250)

    label_info_two = Tk.Label(master=text_post, text=DESCRIPTION_ALGORITHM_POST_TWO, justify="left",
                              font=("Bahnschrift Light", "16"), background="white")
    label_info_two.place(x=5, y=350)
    objects.append(label_info_two)

    img_tablep = Image.open(Path.cwd() / "Image" / "tablep.png")
    photo_tablep = ImageTk.PhotoImage(img_tablep, master=text_post)
    label_tablep = Tk.Label(text_post, image=photo_tablep)
    label_tablep.image = photo_tablep
    label_tablep.place(x=740, y=410)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_for_algorithms)
    label_exit = Tk.Label(window_for_algorithms, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_for_algorithms, image=photo_exit, width=40, height=40, background="white",
                            relief="flat", cursor="hand2", command=lambda: menu_post(objects, dict_windows))
    button_exit.place(x=5, y=705)
    objects.append(button_exit)


def create_window_post_control(dict_windows):
    dict_windows["window_for_algorithms"].withdraw()
    window_control_post = control_post.create_control_post(dict_windows)


def create_menu_for_algorithms_post(dict_windows):
    window_for_algorithms, dict_windows = menu_for_algorithms(dict_windows)
    objects = []
    menu_post(objects, dict_windows)


def menu_post(objects, dict_windows):  # меню для работы с машиной Псота
    window_for_algorithms = dict_windows.get("window_for_algorithms")
    objects = destroy_objects(objects)

    window_for_algorithms.title("Машина Поста")
    # создание title
    img_fon = Image.open(Path.cwd() / "Image" / "Фон2.png")
    photo_fon = ImageTk.PhotoImage(img_fon, master=window_for_algorithms)
    label_fon = Tk.Label(window_for_algorithms, image=photo_fon)
    label_fon.image = photo_fon
    canvas = Tk.Canvas(master=window_for_algorithms, width=1200, height=375)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, anchor="nw", image=photo_fon)
    objects.append(canvas)

    frame_button = Tk.Frame(master=window_for_algorithms, width=1200, height=375, background="white")
    frame_button.place(x=0, y=375)
    objects.append(frame_button)

    label_title = Tk.Label(master=window_for_algorithms, text="Машина Поста", justify="left", width="25", height=1,
                           font=("Gabriola", "48", "bold"), background=rgb_hack((1, 116, 64)))
    label_title.pack(pady=(300, 200))
    objects.append(label_title)
    # создание кнопок для работы с машиной Поста
    img_theory = Image.open(Path.cwd() / "Image" / "theory.png")
    photo_theory = ImageTk.PhotoImage(img_theory, master=window_for_algorithms)
    label_theory = Tk.Label(window_for_algorithms, image=photo_theory)
    label_theory.image = photo_theory
    button_theory = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_theory, width=200, height=200,
                              cursor="hand2", command=lambda: brief_reference_post(objects, dict_windows))
    button_theory.place(x=125, y=450)
    objects.append(button_theory)

    img_algorithm = Image.open(Path.cwd() / "Image" / "training.png")
    photo_algorithm = ImageTk.PhotoImage(img_algorithm, master=window_for_algorithms)
    label_algorithm = Tk.Label(window_for_algorithms, image=photo_algorithm)
    label_algorithm.image = photo_algorithm
    button_algorithm = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_algorithm, width=200,
                                 height=200, cursor="hand2",
                                 command=lambda: description_algorithm_post(objects, dict_windows))
    button_algorithm.place(x=375, y=450)
    objects.append(button_algorithm)

    img_trainer = Image.open(Path.cwd() / "Image" / "trainer.png")
    photo_trainer = ImageTk.PhotoImage(img_trainer, master=window_for_algorithms)
    label_trainer = Tk.Label(window_for_algorithms, image=photo_trainer)
    label_trainer.image = photo_trainer
    button_trainer = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_trainer, width=200, height=200,
                               cursor="hand2", command=lambda: create_window_machine_post(dict_windows))
    button_trainer.place(x=625, y=450)
    objects.append(button_trainer)

    img_control = Image.open(Path.cwd() / "Image" / "control.png")
    photo_control = ImageTk.PhotoImage(img_control, master=window_for_algorithms)
    label_control = Tk.Label(window_for_algorithms, image=photo_control)
    label_control.image = photo_control
    button_control = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_control, width=200, height=200,
                               cursor="hand2", command=lambda: create_window_post_control(dict_windows))
    button_control.place(x=875, y=450)
    objects.append(button_control)

    img_exit = Image.open(Path.cwd() / "Image" / "exit.png")
    photo_exit = ImageTk.PhotoImage(img_exit, master=window_for_algorithms)
    label_exit = Tk.Label(window_for_algorithms, image=photo_exit)
    label_exit.image = photo_exit
    button_exit = Tk.Button(master=window_for_algorithms, relief="flat", image=photo_exit, width=40, height=30,
                            cursor="hand2", background="white", command=lambda: return_first_form(dict_windows))
    button_exit.place(x=5, y=710)
    objects.append(button_exit)

    window_for_algorithms.protocol("WM_DELETE_WINDOW", lambda: return_first_form(dict_windows))
