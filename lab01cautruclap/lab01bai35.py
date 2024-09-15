# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:14:40 2024

@author: nhuy
"""

print("Tinh S = 1 + 2 + 3 +...+n")
n=int(input("Nhap n: "))
if n>0:
    s=0
    for i in range (1,n+1):
        s+=i
    print(s)
else:
    print("Nhap sai, nhap lai.")
