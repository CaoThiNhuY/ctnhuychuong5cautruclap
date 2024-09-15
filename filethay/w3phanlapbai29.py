# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:45:24 2024

@author: Admin
"""

import math
n = int(input("Nhap so nguyen duong n: "))

def songuyento(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if math.gcd(i, j) == 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
songuyento(n)
