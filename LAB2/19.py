import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
win = tk.Tk()
win.title("Python GUI")


tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1,fill='both')
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')  
mighty.grid(column=0, row=0, padx=8, pady=4)
def click_me():
    action.configure(text='hello ' + nameMy.get() + ' ' + mynumber.get())
   
    

a_label = ttk.Label(mighty,text='enter a name:')
a_label.grid(column=0,row=0, sticky='W')

b_label = ttk.Label(mighty,text='choose a number')
b_label.grid(column=1,row=0)

action = ttk.Button(mighty,text='click me',command=click_me)
action.grid(column=2,row=1)

nameMy = tk.StringVar()
name_entered = ttk.Entry(mighty,width=12,textvariable=nameMy)
name_entered.focus()
name_entered.grid(column=0,row=1, sticky='W')

mynumber = tk.StringVar()
number_choosen = ttk.Combobox(mighty,width=12,textvariable=mynumber)
number_choosen['value'] = (1,2,3,4,5,100,32)
number_choosen.current(0)
number_choosen.grid(column=1,row=1)

mighty2 = ttk.LabelFrame(tab2, text='The Snake ')  
mighty2.grid(column=0, row=0, padx=8, pady=4,sticky=tk.W,columnspan=3)
var_check_1 = tk.IntVar()
checkbox_1 = tk.Checkbutton(mighty2,text='diabled',variable=var_check_1,state='disabled')
checkbox_1.select()
checkbox_1.grid(column=0,row=0,sticky='w')

var_check_2 = tk.IntVar()
checkbox_2 = tk.Checkbutton(mighty2,text='uncheck',variable=var_check_2)
checkbox_2.deselect()
checkbox_2.grid(column=1,row=0,sticky='w')

var_check_3 = tk.IntVar()
checkbox_3 = tk.Checkbutton(mighty2,text='enable',variable=var_check_3)
checkbox_3.select()
checkbox_3.grid(column=2,row=0,sticky='w')

def handleRadio():
    color_value = var_radio.get()
    if(color_value == 1):
        win.configure(background=COLOR1)
    elif(color_value == 2):
        win.configure(background=COLOR2)
    elif(color_value == 3):
        win.configure(background=COLOR3)


COLOR1 = "Blue"  
COLOR2 = "Gold"  
COLOR3 = "Red"

var_radio = tk.IntVar()

radio_1 = tk.Radiobutton(mighty2,text =COLOR1,variable=var_radio,value=1,command=handleRadio)
radio_1.grid(column=0,row=4,sticky='w')


radio_2 = tk.Radiobutton(mighty2,text =COLOR2,variable=var_radio,value=2,command=handleRadio)
radio_2.grid(column=1,row=4,sticky='w')


radio_3 = tk.Radiobutton(mighty2,text =COLOR3,variable=var_radio,value=3,command=handleRadio)
radio_3.grid(column=2,row=4,sticky='w')

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0,row=3, columnspan=3)


# # labelfram
buttons_frame = ttk.LabelFrame(mighty2,text='labels in a Frame')
buttons_frame.grid(column=0,row=7,)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0,  sticky=tk.W)

# menu
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label = 'New')
file_menu.add_separator()

file_menu.add_command(label = 'Exit')

menu_bar.add_cascade(label="File", menu=file_menu)



file_menu2 = Menu(menu_bar, tearoff=0)
file_menu2.add_command(label = 'about')
menu_bar.add_cascade(label="Help", menu=file_menu2)
win.mainloop()