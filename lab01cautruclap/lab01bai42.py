# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:38:50 2024

@author: nhuylap01
"""

print("S(n) = 1/1*2 + 1/2*3 +...+1/n*(n+1)")
n=int(input("Nhap so nguyen duong n: "))
if n>0:
    s=0
    for i in range(1,n+1):
        s=s+(1/(i*(i+1)))
    print(s)
else:
    print("Nhap sai, nhap lai.")
