# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:16:23 2023

@author: lab
"""

class animal:
    def __init__(self,raza,nombre,edad):
        self.raza=raza
        self.nombre=nombre
        self.edad=edad
    def d(self):
        print( self.nombre ,"esta durmiendo")
    def des(self):
        print(self.nombre,"se desperto")
    def comer(self):
        print(self.nombre,"esta comiendo")
        
        
perro=animal("french","juan",2)
perro.d()
perro.des()
perro.comer()


# 