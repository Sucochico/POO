# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:21:04 2023

@author: lab
"""

class mascota:
    def __init__(self,nombre,tamaño,edad,raza):
        self.nombre=nombre
        self.tamaño=tamaño
        self.edad=edad
        self.raza=raza
        
    def despertarse(self):
        print(self.nombre,"se ha despertado")
        
    def dormir(self):
        print(self.nombre,"esta dormido")
        
    def comer(self,comida):
        print(self.nombre,"esta comiendo",comida)
        
    def correr(self):
        print(self.nombre,"a empezado a correr")
        
    def sentarse(self):
        print(self.nombre,"se ha sentado")
        
m1=mascota("mike", "90 cm ", "2 años","pitbull")
m1.despertarse()
m1.sentarse()
m1.comer("croquetas")
m1.correr()
m1.dormir()        