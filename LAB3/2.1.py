import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

def _msgBox():
    msg.showinfo('A Python Gui created using tkinter:The Year is 2021')
   


win = tk.Tk()
win.title("TK")
_msgBox()

win.mainloop()