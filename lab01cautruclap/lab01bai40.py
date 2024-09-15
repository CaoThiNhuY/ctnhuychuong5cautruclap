# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:26:00 2024

@author: lab01nhuy
"""

print("S(n) = 1/2 + 1/4 +...+ 1/n")
n=int(input("Nhap so nguyen duong n: "))
if n>0 and n%2==0:
    s=0
    for i in range(1,n+1,1):
        s=s+(1/(2*i))
    print(s)
else:
    print("Nhap sai, nhap lai.")
