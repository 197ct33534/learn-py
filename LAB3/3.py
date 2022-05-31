import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

win = tk.Tk()
def _msgBox():
    msg.showinfo('This is a Title','A Python Gui created using tkinter:\nThe Year is 2021')
   

def createExit():
    win.destroy()
# menu
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label = 'New')
file_menu.add_separator()

file_menu.add_command(label = 'Exit',command=createExit)

menu_bar.add_cascade(label="File", menu=file_menu)



file_menu2 = Menu(menu_bar, tearoff=0)
file_menu2.add_command(label = 'about',command=_msgBox)
menu_bar.add_cascade(label="Help", menu=file_menu2)


tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1,fill='both')
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')  
mighty.grid(column=0, row=0, padx=8, pady=4)

buttons_frame = ttk.LabelFrame(mighty,text='labels in a Frame')
buttons_frame.grid(column=0,row=7,)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0,  sticky=tk.W)

win.title("Python GUI")
_msgBox()

win.mainloop()