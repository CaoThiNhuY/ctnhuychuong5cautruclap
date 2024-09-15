# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:04:39 2024

@author: lap01-lap
"""

n=int(input("Nhap so n nguyen duong: "))
tong=0
while n>0:
    tong+=n%10
    n//10
print("Tong cac chu so",tong)
