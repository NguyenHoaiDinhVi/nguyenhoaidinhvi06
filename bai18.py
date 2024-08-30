# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:45:11 2024

@author: Admin
"""

print("nhập giờ phút giây thứ nhất")
a=int(input("giờ:"))
b=int(input("phút:"))
c=int(input("giây:"))
print("nhập giờ phút giây thứ hai")
d=int(input("giờ:"))
e=int(input("phút:"))
f=int(input("giây:"))
q=(a*3600)+(b*60)+c
w=(d*3600)+(e*60)+f
cong=q+w
tru=q-w
gio1=cong//3600
phut1=(cong%3600)//60
giay1=(cong%3600)%60

gio2=tru//3600
phut2=(tru%3600)//60
giay2=((tru%3600)%60)
print("hai giờ cộng lại:",gio1,":",phut1,":",giay1)
print("hai giờ trừ nhau:",gio2,":",phut2,":",giay2)