# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:24:08 2024

@author: Admin
"""

print("Tinh S = 1 * 2 * 3 * ... * n (voi n le > 0)")
n=int(input("Nhap so nguyen duong n: "))
if n>0 and n%2!=0:
    s=1 
    for i in range(1,n+1,1):
        s*=i
    print(s)
else:
    print("Nhap sai, nhap lai.")
