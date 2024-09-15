# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:36:59 2024

@author: ctnhuy
"""

n=int(input("Nhap so nguyen duong n:"))
giay_thua=1
for i in range(1,n+1):
    giay_thua=giay_thua*i
print("Giay thua cua {} la {}".format(n,giay_thua))