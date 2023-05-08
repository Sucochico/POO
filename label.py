
import tkinter as tk

root=tk.Tk()
root.geometry('300x200')

label=tk.Label(root,text='ingresa tu nombre:')
label.pack()

var1=tk.BooleanVar()
var1.set(False)

var2=tk.BooleanVar()
var2.set(False)

def seleccionado():
    opciones=[]
    if var1.get():
        opciones.append('opcion1')
    if var2.get():
        opciones.append('opcion2')
    label.config(text=f"seleccionaste {','.join(opciones)}")


rb1=tk.Checkbutton(root,text='opcion 1', variable=var1,offvalue=False, command=seleccionado())
rb1.pack()

entry=tk.Entry(root,width=30)
entry.pack()

root.mainloop()

