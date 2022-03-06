from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def body(size):
    root = tk.Tk()
    root.geometry(size)
    root.title("DAR FIT")
    root.resizable(False, False)

    # Configure Grid in APP
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.rowconfigure(0, weight=2)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=2)
    root.rowconfigure(4, weight=2)
    root.rowconfigure(5, weight=2)
    root.rowconfigure(6, weight=2)
    root.rowconfigure(7, weight=2)
    root.rowconfigure(8, weight=2)
    root.rowconfigure(9, weight=2)
    root.rowconfigure(10, weight=2)

    # Logo
    logo = Image.open('logo_app.png')
    logo.thumbnail((150, 150))
    logo = ImageTk.PhotoImage(logo)
    logo_label = ttk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(row=0, columnspan=4)

    # Style label
    var = StringVar()
    label = Label(root, font="Red", bd=3)

    # Buttons
    label1 = ttk.Label(root, text='   Day\nReview', font=18)
    label1.grid(column=0, row=1)
    label2 = ttk.Label(root, text='  Week\nReview', font=18)
    label2.grid(columnspan=4, row=1)
    label3 = ttk.Label(root, text=' Month\nReview', font=18)
    label3.grid(column=3, row=1)
    button_training1 = ttk.Button(root, text='Training')
    button_training1.grid(column=0, row=2)
    button_training2 = ttk.Button(root, text='Training')
    button_training2.grid(columnspan=4, row=2)
    button_training3 = ttk.Button(root, text='Training')
    button_training3.grid(column=3, row=2)
    button_diet1 = ttk.Button(root, text='Diet')
    button_diet1.grid(column=0, row=3)
    button_diet2 = ttk.Button(root, text='Diet')
    button_diet2.grid(columnspan=4, row=3)
    button_diet3 = ttk.Button(root, text='Diet')
    button_diet3.grid(column=3, row=3)
    button_time1 = ttk.Button(root, text='Emotions')
    button_time1.grid(column=0, row=4)
    button_time2 = ttk.Button(root, text='Emotions')
    button_time2.grid(columnspan=4, row=4)
    button_time3 = ttk.Button(root, text='Emotions')
    button_time3.grid(column=3, row=4)
    button_question1 = ttk.Button(root, text='   Question to Coach   ')
    button_question1.grid(column=0, row=5)
    button_question2 = ttk.Button(root, text=' Question to Dietician ')
    button_question2.grid(column=0, row=6)
    button_exit = ttk.Button(root, text='Exit', command=lambda: root.quit())
    button_exit.grid(column=3, row=9)
    button_help = ttk.Button(root, text='Help')
    button_help.grid(column=0, row=9)

    # Buttons day review
    root.mainloop()


# size 500x400
body("500x400")
