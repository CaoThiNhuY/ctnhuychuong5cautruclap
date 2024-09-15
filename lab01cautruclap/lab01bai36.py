# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:18:23 2024

@author: nhuylab01
"""

print("Tinh S = 1*2 + 2*2 + 3*2 + ... + n*2")
n=int(input("Nhap so nguyen duong n: "))
if n>0:
    s=0
    for i in range(1,n+1):
        s=s+(i**2)
    print(s)
else:
    print("Nhap sai, nhap lai.")
