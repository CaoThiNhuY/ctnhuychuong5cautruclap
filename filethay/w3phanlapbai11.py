# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:04:45 2024

@author: w3-phanlap
"""

n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
    print(m,n)
#giá trị của m, n sau khi thực thi
#9 12345678
#98 1234567
#987 123456
#9876 12345
#98765 1234
#987654 123
#9876543 12
#98765432 1
#987654321 0