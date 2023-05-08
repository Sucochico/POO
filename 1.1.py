# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class animal:
    def hablar(self):
        print("haciendo un ruido generico ")
        
class perro(animal):
    def hablar(self):
        super().hablar()
        print("guau ")
        
miperro=perro()
miperro.hablar()