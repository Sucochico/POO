# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:50:37 2023

@author: lab
"""

class robot:
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
        
    def saludar (self):
        print("hola mundo, mi nombre es" ,self.nombre," y he venido a destruirlos")
        
    def despedirse(self):
        print("hasta la vista baby B)")
        
class robotasistente(robot):
    def __init__(self,nombre,color,tareas):
        super().__init__(nombre,color)
        self.tareas=tareas
        
    def saludar(self):
        super().saludar()
        print("hola me llamo" , self.nombre,"soy un robot y ya valiste cheto")
        
    def realizartarea(self):
        print("realizando",self.tareas)
        

robot2=robotasistente("juan", "rojo",["limpiar","cocinar"])
robot2.saludar()
robot2.realizartarea()

