# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:08:55 2024

@author: nhuy
"""

n = int(input("Nhap so nguyen n: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print() 