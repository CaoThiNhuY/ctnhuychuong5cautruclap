# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:30:02 2024

@author: Admin
"""

def print_binary(n):
    binary = bin(n)[2:]
    print(binary)

n = int(input("Nhap so nguyen duong n: "))

if n > 0:
    print_binary(n)
else:
    print("Vui long nhap mot so nguyen duong.")