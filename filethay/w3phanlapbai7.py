# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:24:23 2024

@author: w3-phanlap
"""
count=0
for i in range(1000,2000):
    print(i,end=' ')
    count=count+1
    if count % 5 == 0:
        print()
