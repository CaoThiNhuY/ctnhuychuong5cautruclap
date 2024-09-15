# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:15:58 2024

@author: nhuy
"""

email = input("Moi nhap email: ")

# Kiểm tra xem email có chứa "@" không
if "@" in email:
    # Tách chuỗi email thành 2 phần trước và sau "@"
    user, domain = email.split("@", 1)
    
    # Kiểm tra độ dài của phần trước "@"
    if len(user) < 6:
        print("Email khong hop le: phan truoc @ phai co it nhat 6 ky tu.")
    else:
        # Kiểm tra xem phần trước "@" có chứa khoảng trắng hoặc ký tự đặc biệt
        ktdb = "!@#$%^&*()-=+"
        x = True  # Biến để theo dõi tính hợp lệ
        for char in user:
            if char in ktdb or char == " ":
                x = False
                print("Email khong hop le: phan truoc @ chua ky tu đac biet hoac khoang trang.")
                break
        
        if x:
            # Kiểm tra xem phần sau "@" có chứa dấu chấm "."
            if "." in domain:
                print(f"{email} la mot email hop le.")
            else:
                print("Email khong hop le: phan ten mien sau @ phai chua dau cham.")
else:
    print("Email khong hop le: thieu ky tu @.")