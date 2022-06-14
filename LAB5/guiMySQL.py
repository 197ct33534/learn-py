import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
import mysql.connector
class OOP:
    def __init__(self):
        self.win = tk.Tk()
        
        self.win.title("Python GUI") 

        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='MySQL')
        tabControl.add(tab2, text='Widgets')
        tabControl.pack(expand=1,fill='both')
        mighty = ttk.LabelFrame(tab1, text='Python Database ')  
        mighty.grid(column=0, row=0, padx=8, pady=4)

        

        a_label = ttk.Label(mighty,text='BookTitle')
        a_label.grid(column=0,row=0, sticky='W')

        b_label = ttk.Label(mighty,text='Page')
        b_label.grid(column=1,row=0)

      

        insertQuote1 = tk.StringVar()
        fiel1 = ttk.Entry(mighty,width=30,textvariable=insertQuote1)
        fiel1.focus()
        fiel1.grid(column=0,row=1, sticky='W',padx= 12,pady=5)

        insertQuote2 = tk.StringVar()
        fiel2 = ttk.Entry(mighty,width=30,textvariable=insertQuote2)
        fiel2.focus()
        fiel2.grid(column=0,row=2, sticky='W',padx= 12,pady=5)

        insertQuote3 = tk.StringVar()
        fiel3 = ttk.Entry(mighty,width=30,textvariable=insertQuote3)
        fiel3.focus()
        fiel3.grid(column=0,row=3, sticky='W',padx= 12,pady=5)


        insertQuote4 = tk.StringVar()
        fiel4 = ttk.Entry(mighty,width=12,textvariable=insertQuote4)
        fiel4.focus()
        fiel4.grid(column=1,row=1, sticky='W')

        insertQuote5 = tk.StringVar()
        fiel5 = ttk.Entry(mighty,width=12,textvariable=insertQuote5)
        fiel5.focus()
        fiel5.grid(column=1,row=2, sticky='W')

        insertQuote6 = tk.StringVar()
        fiel6 = ttk.Entry(mighty,width=12,textvariable=insertQuote6)
        fiel6.focus()
        fiel6.grid(column=1,row=3, sticky='W')
       
        mighty2 = ttk.LabelFrame(tab1, text='book  quote ')  
        mighty2.grid(column=0, row=1, padx=8, pady=4)
        scrol_w = 40
        scrol_h = 10
        scr = scrolledtext.ScrolledText(mighty2, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        scr.grid(column=0,row=3, columnspan=3,sticky='WE')
        
        def insertQuote():
            title = insertQuote1.get()
            page = insertQuote4.get()
            # test = scrolledtext.get()
            scr.insert(tk.INSERT,title +" " +page+ '\n')
            self.insert(title,page)
        button1 = ttk.Button(mighty,text='insert quote',command=insertQuote)
        button1.grid(column=2,row=1,padx=5)

        button2 = ttk.Button(mighty,text='get quote')
        button2.grid(column=2,row=2,padx=5)

        button3 = ttk.Button(mighty,text='mody quote')
        button3.grid(column=2,row=3,padx=5)
    def insert(self,matudien,tentudien):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quanlysinhvien"
            
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO tudien (matudien, tentudien) VALUES (%s, %s)"
        val = (matudien, tentudien)
        mycursor.execute(sql, val)

        
oop1 =  OOP()
oop1.win.mainloop()