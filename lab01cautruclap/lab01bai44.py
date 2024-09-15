# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:33:10 2024

@author: Admin
"""

print("S(n) = 1/2 + 3/4 +...+ (2n+1)/(2n+2)")
n=int(input("Nhap so nguyen duong n: "))
if n>=0:
    s=0
    for i in range(0,n+1):
        s=s+((2*i+1)/(2*i+2))
    print(s)
else:
    print("Nhap sai, nhap lai.")
