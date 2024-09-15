# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:58:47 2024

@author: w3phanlap
"""

n=1000000
total= 0.0
#câu a
for i in range(1, n+1):
    total += 1 / (i*i)
#câu b
for i in range(1, n+1):
    total += 1.0 / i*i
#câuc
for i in range(1, n+1):
    total += 1.0 / (i*i)
#câud
for i in range(1, n+1):
    total += 1 / (1.0*i*i)
# Sau khi thử 4 đáp án thì a.c.d đều ra kết quả tương ứng với tổng dạng 1/(i^i) còn đáp án b thì không