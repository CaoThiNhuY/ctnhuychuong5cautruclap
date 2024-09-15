# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:33:47 2024

@author: nhuy
"""

import random

luachon = ["Keo", "Bua", "Bao"]

while True:
    #Máy chọn
    may = random.choice(luachon)
    
    # Người chọn
    nguoi = input("Chon Keo, Bua hoac Bao (hoac go 'Exit' de dung): ")

    # Kiểm tra nếu người dùng muốn thoát
    if nguoi.lower() == 'thoat':
        print("Cam on ban đa choi tro choi!")
        break

    # Kiểm tra xem lựa chọn của người dùng có hợp lệ không
    if may not in luachon:
        print("Lua chon khong hop le. Vui long chon lai!")
        continue

    # In lựa chọn của máy và người chơi
    print(f"Ban chon: {nguoi}")
    print(f"May chon: {may}")

    # Kiểm tra kết quả dựa trên quy tắc trò chơi
    if nguoi == may:
        print("Hoa!")
    elif (nguoi == "Keo" and may == "Bao") or \
         (nguoi == "Bua" and may == "Keo") or \
         (nguoi == "Bao" and may == "Bua"):
        print("Ban thang!")
    else:
        print("May thang!")
    # In dòng ngăn cách
    print("-" * 30)  