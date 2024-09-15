# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:00:47 2024

@author: nhuylab01
"""
while True:
    try:
        # Nhập tháng và năm
        thang = int(input("Nhap thang (1-12): "))
        nam = int(input("Nhap nam: "))
        
        # Kiểm tra tháng có hợp lệ không
        if thang<1 or thang>12:
            print("Thang khong hop le, vui long nhap lai.")
        else:
        # Kiểm tra xem có phải năm nhuận không
            if (nam % 400 == 0) or (nam % 100 != 0 and nam % 4 == 0):
                nam_nhuan = True
            else:
                nam_nhuan = False

        # Xác định số ngày trong tháng
            if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
                ngay = 31
            elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
                ngay = 30
            elif thang == 2:
                if nam_nhuan:
                    ngay = 29
                else:
                    ngay = 28

        # In ra số ngày của tháng
        print("Thang {0} nam {1} co {2} ngay.".format(thang,nam,ngay))
        break
    except ValueError:
        print("Vui long nhap so hop le cho thang va nam.")
