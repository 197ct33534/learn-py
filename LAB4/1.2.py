import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()
strData.set("Hello StringVar")

vardata = strData.get()
print(vardata)