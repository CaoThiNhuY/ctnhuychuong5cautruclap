# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:00:10 2024

@author: Admin
"""

x=float(input("Nhap so thuoc khoang [-89.9;88.8]:"))

while x<-89.9 or x>88.8:
    x=float(input("Nhap lai x:"))
print("Gia tri da nhap:",x)