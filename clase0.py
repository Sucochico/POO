# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:18:26 2023

@author: lab
"""

class Persona :
    def __init__(self,nombre,apellido,genero):
        self.name=nombre
        self.apellido=apellido
        self.genero=genero
        
estudiante =Persona("andy", "mora", "masculino")
profesor=Persona("carlos", "ayala", "masculino")



class animal:
    def __init__(self,nombre,raza,edad,dueño):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.dueño=dueño
        
vaca=animal("lalo", "mamifero", 2, "juan")

