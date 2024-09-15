# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:17:03 2024

@author: Admin
"""
#For
#ví dụ 1
colors=["Do","Cam","Vang","Luc","Lam","Cham","Tim"]
for i in colors:
    print(i,"\t", len(i))
#ví dụ 2
for i in range(10):
    print(i, end='\t')
for i in range(1,10,2):
    print(i, end='\t')
# ứng dụng for để tạo list mới
# ví dụ 3
ds=[2,4,6,8,10]
new_ds=[item - 1 for item in ds]
print(new_ds)
#while
#Ví dụ 1
x=float(input("Nhap x="))
while x<0 :
    x=float(input("Nhap lai x="))
print("Gia tri da nhap:",x)
#ví dụ 2
count=0
n=int(input("Nhap vao so lan can nhap:"))
while (count < 0):
    print("Lan thu nhat:", count+1,"\tBien dem:",count)
    count=count+1
#While có else
#ví dụ 1
x= float(input("Nhap x="))
while x<0:
    x=float(input("Nhap lai x="))
else:
    print("Gia tri da nhap:",x)
#ví dụ 2
count=0
n=int(input("Nhap vao so lan can nhap:"))
while (count < 0):
    print("Lan thu nhat:", count+1,"\tBien dem:",count)
    count=count+1
else:
    print("\nThuc hien lenh trong else,do:",
          "\ncount=", count,"\nn= ", n,
          "\nbool(conut < n)=", bool(count<n))
#break
#ví dụ 1
tup=("Do","Cam","Vang","Luc","Lam","Cham","Tim")
for i in tup: 
    print(i, "\t") 
    if i == "Luc":
        break
#continue
#ví dụ
tup=('Do','Cam','Vang','Luc','Lam','Cham','Tim')
for i in tup: 
    if i =='Vang' or i=='Lam': 
        continue 
    print(i)
#pass
#ví dụ
colors=["Do","Cam","Vang","Luc","Lam","Cham","Tim"]
for i in colors:
    pass