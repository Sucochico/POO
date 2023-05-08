# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 09:18:41 2023

@author: lab
"""
x = 9
 
if x > 5: # True
    if x == 6: # False
        print("anidado: x == 6")
    elif x == 10: # True
        print("anidado: x == 10")
    else:
        print("anidado: else1")
else:
    print("else2")