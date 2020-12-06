# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:35:00 2020

@author: Hansali haitam
"""

def pgcd_Euclide(a,b):
    while a%b != 0:
        n = a
        m = b
        a = m 
        b = n%m
    if a%b == 0:
        return b
