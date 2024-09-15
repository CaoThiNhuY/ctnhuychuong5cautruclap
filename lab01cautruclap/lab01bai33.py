# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:13:49 2024

@author: lab01-lap-nhuy
"""

import math
while True:
    n=int(input("Nhap n: "))
    if n>0:
        sqrt_n=math.isqrt(n)
        if sqrt_n*sqrt_n==n:
            print(n,"la so chinh phuong.")
            break
        else:
            print(n,"khong phai la so chinh phuong.")
            break
    else:
        print("Nhap sai, nhap lai.")