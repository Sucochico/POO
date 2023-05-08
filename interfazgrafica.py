# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:37:31 2023

@author: lab
"""

import tkinter as tk
ventana=tk.Tk()

elementos=["ele1","ele2","ele3"]
ventana.geometry('500x500')
ventana.title('siu')
def clic():
    print("has hecho click")
#def c():
#    print("eres puto")
etiqueta=tk.Label(ventana,text="hola mundo")
etiqueta.pack()
boton1=tk.Button(ventana,text="haga click",command=clic)
boton=tk.Button(ventana,text="haga clic aqui")
#b1=tk.Button(ventana,text="puto el que haga clic",command=c)
ventana.configure(bg="pink")
boton=tk.Button(ventana,text="hagaclic",command=clic)
lista=tk.Listbox(ventana)
for elementos in elementos:
    lista.insert(tk.END, elementos)
lista.pack()
boton1.pack()
#b1.pack()

ventana.mainloop()


