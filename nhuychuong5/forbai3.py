# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:07:42 2024

@author: nhuy
"""
#3a
import random
x=random.randint(20,31)
print("So luong phan tu ngau nhien: ",x)
for i in range(x):
    n=random.randint(20,31)
    print(n)
#3b
import random
x=random.randint(20,31)
print("So luong phan tu ngau nhien: ",x)
danh_sach_binh_phuong=[random.uniform(18,99)**2 for j in range(x)]
print(danh_sach_binh_phuong)
