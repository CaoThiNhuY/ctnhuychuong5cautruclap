# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:42:10 2024

@author: Admin
"""

def fibonacci(n):
    a, b = 0, 1 
    count = 0  

    while count < n:
        print(a, end=", " if count < n - 1 else "\n")  
        a, b = b, a + b  
        count += 1  
fibonacci(100)