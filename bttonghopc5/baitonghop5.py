# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:46:59 2024

@author: nhuy
"""

import random

# Danh sách các lựa chọn
luachon = ["Keo", "Buua", "Bao"]

# Tạo số lượng người chơi ngẫu nhiên từ 8 đến 20
so_luong_nguoi_choi = random.randint(8, 20)

# Tạo danh sách người chơi và lựa chọn của họ
nguoi_choi = []
choices = []

for i in range(so_luong_nguoi_choi):
    player_name = f"Nguoi choi {i + 1}"
    player_choice = random.choice(luachon)
    nguoi_choi.append(player_name)
    choices.append(player_choice)

# In ra số lượng người chơi và lựa chọn của họ
print(f"So nguoi choi: {so_luong_nguoi_choi}\n")
for i in range(so_luong_nguoi_choi):
    print(f"{nguoi_choi[i]} chon: {choices[i]}")

# Tìm người chiến thắng
keo_count = choices.count("Keo")
bua_count = choices.count("Bua")
bao_count = choices.count("Bao")

# Kiểm tra trường hợp hòa (nếu tất cả cùng chọn 1 loại)
if keo_count == so_luong_nguoi_choi or bua_count == so_luong_nguoi_choi or bao_count == so_luong_nguoi_choi:
    print("\nTat ca nguoi choi da chon giong nhau, tran dau hoa!")
else:
    # Xác định chiến thắng dựa trên số lượng
    if keo_count > 0 and bao_count > 0 and bua_count == 0:
        print("\nKeo thang vi co nhieu nguoi chon Keo va khong ai chon Bua!")
    elif bua_count > 0 and keo_count > 0 and bao_count == 0:
        print("\nBua thang vi co nhieu nguoi chon Bua va khong ai chon Bao!")
    elif bao_count > 0 and bua_count > 0 and keo_count == 0:
        print("\nBao thang vi co nhieu nguoi chon Bao va khong ai chon Keo!")
    else:
        # Nếu có tất cả các lựa chọn, sử dụng quy tắc
        if keo_count > bao_count and keo_count > bua_count:
            print("\nKeo thang vi co nhieu nguoi chon Keo hon!")
        elif bua_count > keo_count and bua_count > bao_count:
            print("\nBua thang vi co nhieu người chọn Búa hon!")
        elif bao_count > keo_count and bao_count > bua_count:
            print("\nBao thang vi co nhieu nguoi chon Bao hon!")
        else:
            print("\nKhong co ket qua ro rang, co the can them vong choi khac!")
