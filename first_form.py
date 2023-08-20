
import tkinter as Tk
import services.algorithms as algorithms
from PIL import Image
from tkinter import messagebox


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb


def on_closing():
    if not messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        return
    window.destroy()


def create_window_turing():
    window.withdraw()
    new_window_turing = algorithms.create_menu_for_algorithms_turing(dict_windows)


def create_window_post():
    window.withdraw()
    new_window_post = algorithms.create_menu_for_algorithms_post(dict_windows)


window = Tk.Tk()
window.title("Основы теории алгоритмов")
window_width_center = (window.winfo_screenwidth()) // 2 - 600
window_height_center = (window.winfo_screenheight()) // 2 - 375
window.geometry("1200x750+{}+{}".format(window_width_center, window_height_center))
window.resizable(width=False, height=False)

dict_windows = {"first_window": window}

image = Tk.PhotoImage(file="./Image/Фон.png")

canvas = Tk.Canvas(master=window, width=1200, height=375)
canvas.place(x=0, y=0)

canvas.create_image(0,0, anchor="nw", image=image)

label_title = Tk.Label(master=window, text="Основы теории алгоритмов", justify="center", width="25", height=1, font=("Gabriola", "48", "bold"), bg=rgb_hack((1, 116, 64)))
label_title.pack(pady=(150,75))

frame_button = Tk.Frame(master=window, width=1200, height=375, background="white")
frame_button.place(x=0, y=375)

photo_tur = Tk.PhotoImage(file = "./Image/Кнопка_машина_тьюринга.png")
button_turing_machine = Tk.Button(master=window, font=("Gabriola", "24"), relief="flat" ,image=photo_tur, width=210, height=260, cursor="hand2", command=create_window_turing)
button_turing_machine.place(x=325, y=420)

photo_post = Tk.PhotoImage(file = "./Image/Кнопка_машина_поста.png")
button_post_machine = Tk.Button(master=window, font=("Gabriola", "24"), relief="flat" ,image=photo_post, width=210, height=260, cursor="hand2", command=create_window_post)
button_post_machine.place(x=675, y=420)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
