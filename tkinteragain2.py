import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

window = tk.Tk()
window.geometry('500x600')
window.title('button tutor')

def butt():
    print(value = string1)
string1 = tk.StringVar(value = 'a button with string')
button1 = ttk.Button(window, textvariable = string1, command= butt)
button1.pack()


chckVar = tk.StringVar()
chckVar1 = tk.StringVar()
chckVar2 = tk.StringVar()
checkbutton1 = ttk.Checkbutton(
    window, 
    text = 'new one point',
    command = lambda : print(chckVar.get()),
    variable = chckVar,
    onvalue="malih wooow",
    offvalue="malih jelek")
checkbutton1.pack()
checkbutton2 = ttk.Checkbutton(
    window, 
    text = 'new one point',
    command = lambda : print(chckVar1.get()),
    variable = chckVar1,
    onvalue="malih ganteng",
    offvalue="malih jelek")
checkbutton2.pack()
checkbutton3 = ttk.Checkbutton(
    window, 
    text = 'new one point',
    command = lambda : print(chckVar2.get()),
    variable = chckVar2,
    onvalue="malih ganteng",
    offvalue="malih jelek")
checkbutton3.pack()

radiovalue = tk.StringVar()
radiobutton1 = ttk.Radiobutton(
    window, 
    text="so youre here now",
    command = lambda: print('it pressed'),
    variable= radiovalue ,
    )
radiobutton1.pack()
radiovalue = tk.StringVar()
radiobutton2 = ttk.Radiobutton(
    window, 
    text="so youre here now",
    command = lambda: print('it pressed'),
    variable= radiovalue ,
    )
radiobutton2.pack()

window.mainloop()