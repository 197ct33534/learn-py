import tkinter as tk

win = tk.Tk()

doubleDATA = tk.DoubleVar()

print(doubleDATA.get())
doubleDATA.set(2.5)

print(type(doubleDATA))

add_doubles = 1.2222 + doubleDATA.get()

print(add_doubles)
print(type(add_doubles))