# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:34:58 2024

@author: Admin
"""
#1
for i in range(2020,3939):
    if i & 2 ==0:
        if i != 0 and i & 9 == 0:
            print(i)
#2
print('\t'.join(str(i) for i in range(2020,3939) if i % 2 == 0))