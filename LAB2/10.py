import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")

mighty = ttk.LabelFrame(win, text=' Mighty Python ')  
mighty.grid(column=0, row=0, padx=8, pady=4)

def click_me():
    action.configure(text='hello ' + nameMy.get() + ' ' + mynumber.get())
   
    

a_label = ttk.Label(mighty,text='enter a name:')
a_label.grid(column=0,row=0)

b_label = ttk.Label(mighty,text='choose a number')
b_label.grid(column=1,row=0)

action = ttk.Button(mighty,text='click me',command=click_me)
action.grid(column=2,row=1)

nameMy = tk.StringVar()
name_entered = ttk.Entry(mighty,width=12,textvariable=nameMy)
name_entered.focus()
name_entered.grid(column=0,row=1)

mynumber = tk.StringVar()
number_choosen = ttk.Combobox(mighty,width=12,textvariable=mynumber)
number_choosen['value'] = (1,2,3,4,5,100,32)
number_choosen.current(0)
number_choosen.grid(column=1,row=1)

var_check_1 = tk.IntVar()
checkbox_1 = tk.Checkbutton(mighty,text='diabled',variable=var_check_1,state='disabled')
checkbox_1.select()
checkbox_1.grid(column=0,row=2,sticky=tk.W,columnspan=3)

var_check_2 = tk.IntVar()
checkbox_2 = tk.Checkbutton(mighty,text='uncheck',variable=var_check_2)
checkbox_2.deselect()
checkbox_2.grid(column=1,row=2,sticky=tk.W,columnspan=3)

var_check_3 = tk.IntVar()
checkbox_3 = tk.Checkbutton(mighty,text='enable',variable=var_check_3)
checkbox_3.select()
checkbox_3.grid(column=2,row=2,sticky=tk.W,columnspan=3)

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

radio_1 = tk.Radiobutton(mighty,text =COLOR1,variable=var_radio,value=1,command=handleRadio)
radio_1.grid(column=0,row=4,sticky=tk.W,columnspan=3)


radio_2 = tk.Radiobutton(mighty,text =COLOR2,variable=var_radio,value=2,command=handleRadio)
radio_2.grid(column=1,row=4,sticky=tk.W,columnspan=3)


radio_3 = tk.Radiobutton(mighty,text =COLOR3,variable=var_radio,value=3,command=handleRadio)
radio_3.grid(column=2,row=4,sticky=tk.W,columnspan=3)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0,row=3, columnspan=3)


# labelfram
buttons_frame = ttk.LabelFrame(mighty,text='labels in a Frame')
buttons_frame.grid(column=1,row=7,)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0,  sticky=tk.W)



win.mainloop()