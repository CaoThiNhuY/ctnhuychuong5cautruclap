# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:40:42 2024

@author: w3-phanlap
"""
import random
n=int(input("Nhap mot so nguyen n :"))
so=[0] * n
for i in range(n):
    so[i]=random.random()
tb=sum(so)/len(so)
max_so=max(so)
min_so=min(so)
print(f"Gia tri trung binh la: {tb}")
print(f"Gia tri lon nhat la: {max_so}")
print(f"Gia tri nho nhat la: {min_so}")