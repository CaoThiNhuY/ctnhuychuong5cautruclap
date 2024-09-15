# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:56:35 2024

@author: w3-phanlap-bai5
"""

#a. 
    #```python
j = 0
for i in range(0, 10):
    j += i
print(j)
#giá trị j sau khi thực thi: 45
#b. 
j = 1
for i in range(0, 10):
    j += j
print(j)
#giá trị j sau khi thực thi: 1024
#c
for j in range(0, 10):
    j += j
print(j)
##giá trị j sau khi thực thi: 18