import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


# window
window = ttk.Window(themename='journal')
window.title('demo')
window.geometry('300x130')

#title
title_label = ttk.Label(master = window, text = 'miles to kilometer', font = 'ignotum 24 italic')
title_label.pack(pady = 10)

#function
def convert():
    print(entry_int.get())
    inch_input = entry_int.get()
    cm_output = inch_input * 2.54
    output_super.set(cm_output)
# function_convert = 

#input field
input_main = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_main, textvariable = entry_int)
button = ttk.Button(master = input_main, text = 'Convert',command = convert)
title_inch = ttk.Label(master = input_main, text = 'inch', font = 'courier 15')
button.pack(side = 'left', padx = 5)
entry.pack(side = 'left', padx = 10)
title_inch.pack(side = 'left', padx = 5)
input_main.pack(pady = 5)

#output
output_main = ttk.Frame(master = window)
output_super = tk.StringVar()
output_labal = ttk.Label(master = output_main, text = 'Output', 
                         font = 'courier 15', textvariable = output_super)
output_centi = ttk.Label(master = output_main, text= 'cm', font = 'courier 15')
output_labal.pack(side= 'left')
output_centi.pack(side = 'left')
output_main.pack()


#run mainloop
window.mainloop()