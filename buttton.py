# button in app
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("500x400")
root.title("Training Review for Day")
root.resizable(False, False)


def day_training():
    data = inputtxt.get("1.0", "end-1c")
    print(data)


l_data = Label(text="Waht's data today?")
inputtxt = Text(root, height=2,
                width=100,
                bg="white")
Output = Text(root, height=5,
              width=5,
              bg="white")

Display = Button(root, height=2,
                 width=5,
                 text="Show",
                 command=lambda: day_training())

l_data.pack()
inputtxt.pack()
Display.pack()
Output.pack()

root.mainloop()
