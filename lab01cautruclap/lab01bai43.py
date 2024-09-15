# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:29:46 2024

@author: nhuylab01
"""
print("S(n) = 1/2 + 2/3 +...+ n/n+1")
n=int(input("Nhap so nguyen duong n: "))
if n>0:
    s=0
    for i in range(1,n+1):
        s=s+(i/(i+1))
    print(s)
else:
    print("Nhap sai, hap lai.")

