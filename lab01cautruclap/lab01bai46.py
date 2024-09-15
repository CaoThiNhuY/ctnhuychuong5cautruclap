# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:42:12 2024

@author: labo1nhuy
"""

for x in range(1,490): # 979/2
    for y in range(1,140): #979/7
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                print("Nghiem cua phuong trinh la:", "x={0}, y={1}, z={2}".format(x,y,z), end="\n")