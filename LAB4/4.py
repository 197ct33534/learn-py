import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *

class ToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='yellow', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


class OOP:
    def __init__(self):
        self.win = tk.Tk()
        
        self.win.title("Python GUI") 

        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tabControl.add(tab2, text='Tab 2')
        tabControl.pack(expand=1,fill='both')
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')  
        mighty.grid(column=0, row=0, padx=8, pady=4)

        

        a_label = ttk.Label(mighty,text='enter a name:')
        a_label.grid(column=0,row=0, sticky='W')

        b_label = ttk.Label(mighty,text='choose a number')
        b_label.grid(column=1,row=0)

      

        nameMy = tk.StringVar()
        name_entered = ttk.Entry(mighty,width=12,textvariable=nameMy)
        name_entered.focus()
        name_entered.grid(column=0,row=1, sticky='W')

        mynumber = tk.StringVar()
        number_choosen = ttk.Combobox(mighty,width=12,textvariable=mynumber)
        number_choosen['value'] = (1,2,3,4,5,100,32)
        number_choosen.current(0)
        number_choosen.grid(column=1,row=1)

        action = ttk.Button(mighty,text='click me',command=self.click_me)
        action.grid(column=2,row=1)

        
            
        spin = Spinbox(mighty,values=(1, 2, 4, 42, 100),width=5,bd=8,command=self._spin)
        spin.grid(column=0, row=2)

        scrol_w = 30
        scrol_h = 3
        scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        scr.grid(column=0,row=3, columnspan=3,sticky='WE')
      
       
        ToolTip(tabControl,"hello gui ")
        ToolTip(spin,"this is a spinbox control ")

    def click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' +self.number_chosen.get()) 
    def create_widgets(self): 
        # Create Tab Control
        tabControl = ttk.Notebook(self.win)  
        tab1 = ttk.Frame(tabControl)  
        tabControl.add(tab1, text='Tab 1') 
        tab2 = ttk.Frame(tabControl)  
        tabControl.add(tab2, text='Tab 2')  
        # Pack to make visible
        tabControl.pack(expand=1, fill="both")
    def _spin():
            value_get = spin.get()
            print(value_get)
            scr.insert(tk.INSERT,value_get + '\n')
        
    def click_me():
            action.configure(text='hello ' + nameMy.get() + ' ' + mynumber.get())
   

oop1 =  OOP()
oop1.win.mainloop()