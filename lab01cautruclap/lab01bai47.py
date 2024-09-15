# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:01:38 2024

@author: nhuylab01
"""

maxsum = 0
nghiemmoi = (0, 0, 0)
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
         if 2*x+7*y+9*z==979:
             sum1=x+y+z
             if sum1>maxsum:
                 maxsum=sum1
                 nghiemmoi=(x,y,z)
print("Nghiem cua phuong trinh la:", "X={0},y={1},z={2}".format(nghiemmoi[0],nghiemmoi[1],nghiemmoi[2]))
print("Tong 3 nghiem lon nhat:", maxsum)
