# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:23:04 2024

@author: nhuylab01lap
"""

print("Tinh S = 2 + 4 + 6 + ... + n (voi n chan > 0)")
n=int(input("Nhap so nguyen duong n: "))
if n>0 and n%2==0:
    s=0
    for i in range(2,n+2,2):
        s=s+i
    print(s)
else:
    print("Nhap sai, nhap lai.")
