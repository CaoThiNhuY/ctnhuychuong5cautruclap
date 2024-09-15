# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:07:23 2024

@author: lab01-lap
"""

s=float(input("Quang duong di dc (km): "))
if s<=1:
    print("Tien taxi: 15000đ")
elif s<=5:
    print("Tien taxi: ", 15000 + (s - 1) * 13500,"đ")
elif s>=120:
    print("Tien taxi: ", (15000 + 4*13500 + (s-1)*11000)*0.9)
else:
    print("Tien taxi: ", 15000 + 4*13500 + (s-1)*11000,"đ")
