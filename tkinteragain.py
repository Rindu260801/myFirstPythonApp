import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import sympy as smp



root = ttk.Window(themename='darkly')
root.title('my first math job')
root.geometry('400x100')

def make():
    x = calculus.get()
    y = x * 200
    outputsuper.set(y)
    text['state'] = 'normal'
    form['state'] = 'normal'

#widget master and label
frame = ttk.Frame(master = root)
label1= ttk.Label(master = frame,text='this is sympy',font='courier 14')
label1.pack(side='left', padx=3)

#command
def change_it():
    label1.config(textvariable= outputsuper)
    form.config(state = 'disable')
    print(label1.configure(textvariable=outputsuper))
    text['state']= 'disable'



#widget button and form
calculus = tk.IntVar()
form = ttk.Entry(master=frame,textvariable=calculus)
button = ttk.Button(master=frame,text ='test',command=make)
form.pack(side='left', padx = 3)
button.pack(side = 'left', padx =3)
button2 = ttk.Button(master = root, text='change me',command = change_it)
frame.pack(pady=10)
outputsuper = tk.StringVar()
output = ttk.Label(master= root, textvariable= outputsuper ,font='courier 14')
output.pack()
button2.pack()


#widget text
text = ttk.Text(master = root)
text.pack()

root.mainloop()