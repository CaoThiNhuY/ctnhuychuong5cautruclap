# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:30:13 2024

@author: Admin
"""

user_id=input("Nhap ID nguoi dung:")
password=input("Nhap mat khau:")
#ID USER
#Độ dài
if len(user_id) <6 or len(user_id) >24:
    print("Do dai khong phu hop. Vui long kiem tra lai!")
else:
    print("Hop le")
#Ký tự đặc biệt
ktdb='!@#$%^&*()-=+'
x=True
for char in user_id:
  if char in ktdb:
    print("Ky tu khong phu hop. Vui long kiem tra lai!", char)
    x=False
    break
if x:
    print("Hop le")
#Khoảng trắng
if ' ' in user_id:
    print("Khong duoc co khoang trang. Vui long nhap lai!")
else:
    print("Hop le")
    
#PASSWORD
#Ít nhất 1 chữ cái nằm trong [a-z]
chuthuong="abcdefghijklmnopqrstuvwxyz"
x=False
for char in password:
    if char in chuthuong:
        x=True
        break
if x:
        print("Hop le")
else:
        print("Khong hop le. Can it nhat 1 chu cai thuong. Vui long kiem tra lai!")
        
#Ít nhất 1 số từ [0-9]
so="123456789"
x=False
for char in password:
    if char in so:
        x=True
        break
if x:
        print("Hop le")
else:
        print("Khong hop le. Can co 1 chu so. Vui long kiem tra lai!")
        
#Ít nhất 1 chữ cái nằm trong [A-Z]
chuhoa="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=False
for char in password:
    if char in chuhoa:
        x=True
        break
if x:
        print("Hop le")
else:
        print("Khong hop le. Can it nhat 1 chu cai thuong. Vui long kiem tra lai!")
        
#ít nhất 1 ký tự trong  [$ # @]
kytu= "$#@"
x=False
for char in password:
    if char in kytu:
        x=True
        break
if x:
        print("Hop le")
else:
        print("Khong hop le. Can it nhat 1 ky tu tren. Vui long kiem tra lai")
        
#Độ dài
if len(password) <6 or len(password) >24:
    print("Do dai khong phu hop. Vui long kiem tra lai!")
else:
    print("Hop le")