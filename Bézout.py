# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:35:14 2020

@author: Hansali haitam
"""

def Bezout(a, b):
    x1 = 1
    x2 = 0
    x3 = 0
    x4 = 1
    while b > 0:
        r = a // b       
        n = a
        
        m = b
        a = m 
        b = n%m  
        
        y1 = x1
        y2 = x2
        y3 = x3
        y4 = x4 
        
        x1 = y3
        x2 = y4
        x3 = y1 - (r*y3)
        x4 = y2 - (r*y4)
    print("Bezout("+str(-x4)+ ", "+str(x3)+") #PGCD:", a, "(u=",x1, ")*",-x4,"+(v=", x2,")*", x3,"=", a)

