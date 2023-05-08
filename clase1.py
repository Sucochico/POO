# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:52:37 2023

@author: lab
"""

class employe:
    count=0
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
        employe.count+=1
    def displaycount(self):
        print("total de empleados",employe.count)
    def displayemploye(self):
        print("nombre: ",self.nombre,"salario: ",self.salario)
            
empleado0=employe("andy", 20)
empleado1=employe("juan", 205)
empleado2=employe("michael", 208)
empleado3=employe("steven", 2100)
empleado4=employe("lucas", 2000)
empleado0.displayemploye()
empleado1.displayemploye()
empleado2.displayemploye()
empleado3.displayemploye()
empleado4.displayemploye()
empleado0.displaycount()
