# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:32:19 2024

@author: Admin
"""

x=float(input("Nhap so thuoc khoang [-99;99]:"))

while x<-99 or x>99:
    x=float(input("Nhap lai x:"))
print("Gia tri da nhap:",x)
    
