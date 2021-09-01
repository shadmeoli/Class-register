# import tkinter module 
from tkinter import * 
from tkinter.ttk import *
from datetime import datetime
from datetime import *
import json
from tkinter import messagebox

# import strftime function to retrieve system's time 
from time import strftime 
from tkinter import ttk
from tkinter.ttk import *

#class
root = Tk() 
root.title('Lesson In progress') 
root.geometry('500x300')
root.resizable(False, False)
root.config(background='LightCyan2')


def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 


def stop_class():
    messagebox.showinfo(f'Ended', 'Class ended')
    root.destroy()
    import app

ongoing = Label(root, text='ON GOING CLASS', foreground='gray', background='LightCyan2', font=('Tahoma', 20))
ongoing.place(x=140, y=30)

lbl = Label(root, font = ('calibri', 20, 'bold'),  
            foreground = 'gray', 
            background= 'LightCyan2'
            ) 

lbl.place(x=160, y=140)
time()

s = ttk.Style()
s.configure('stop.TButton', foreground='red')

stop = Button(root, text='STOP', cursor='X_cursor', command=stop_class, style='stop.TButton')
stop.place(x=200, y=250)

if __name__ == '__main__':
    root.mainloop()