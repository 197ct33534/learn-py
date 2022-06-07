import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
from time import sleep   
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


        mighty2 = ttk.LabelFrame(tab2, text='hello gui ')  
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
                mighty2.configure(text=COLOR1)
            elif(color_value == 2):
                mighty2.configure(text=COLOR2)
            elif(color_value == 3):
                mighty2.configure(text=COLOR3)


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
            # Add a Progressbar to Tab 2
        progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        progress_bar.grid(column=0, row=7, pady=2) 
     # update progressbar in callback loop
        def run_progressbar():
            progress_bar["maximum"] = 100
            for i in range(101):
                sleep(0.05)
                progress_bar["value"] = i   # increment progressbar
                progress_bar.update()       # have to call update() in loop
            progress_bar["value"] = 0       # reset/clear progressbar  

        def start_progressbar():
            progress_bar.start()
            
        def stop_progressbar():
            progress_bar.stop()
        
        def progressbar_stop_after(wait_ms=1000):    
            self.win.after(wait_ms, progress_bar.stop)
   
        
        
    # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=5, sticky='W', columnspan=2)        

        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_progressbar).grid(column=0, row=3, sticky='W')  
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=4, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=5, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=6, sticky='W')  
        
        for child in buttons_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
        
        for child in mighty2.winfo_children():  
            child.grid_configure(padx=8, pady=2) 

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