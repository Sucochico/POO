# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:35:29 2023

@author: lab
"""

class vehiculo:
    def __init__(self,velocidad,posicion,direccion,numruedas):
        self.velocidad=velocidad
        self.posicion=posicion
        self.direccion=direccion
        self.numruedas=numruedas
        
class carro(vehiculo):
    def __init__(self,marca,color,velocidad,posicion,direccion,numruedas):
        super().__init__(velocidad,posicion,direccion,numruedas)
        self.marca=marca
        self.color=color

    def acelerar(self):
        print("el carro esta acelerando a ",self.velocidad,"km/h")
        
    def frenar(self):
        print("el carro esta frenando")
    def posicion(self):
        print("el carro esta en la posicion",self.posicion)
    
class moto(vehiculo):
    def __init__(self,marca,color,velocidad, posicion, direccion, numruedas):
        super().__init__(velocidad, posicion, direccion, numruedas)
        self.marca=marca
        self.color=color
        
    def acelerar(self):
        print("la moto esta acelerando a",self.velocidad,"km/h")
        
    def frenar(self):
        print("la moto esta frenando")
        
    def posicion(self):
        print("la moto esta en la posicion",self.posicion)

v1=carro("bmw","rojo",120,1,"norte",4)
v1.acelerar()
v1.frenar()

v2=moto("yamaha", "negro", 200, 2, "norte", 2)
v2.acelerar()
v2.frenar()
