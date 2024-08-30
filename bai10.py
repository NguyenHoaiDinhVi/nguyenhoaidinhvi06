# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:01:40 2024

@author: Admin
"""

print("tính số nút xe của bạn:")
a=int(input("số nút xe:"))
b=a//1000
c=(a%1000)//100
d=(a%1000)%100//10
e=(a%1000)%100%10
sonutxe=b+c+d+e
if sonutxe<10:
    print("số nút xe của bạn là:", sonutxe)
elif sonutxe>10:
    sonutxe=(sonutxe//10)+(sonutxe%10)
    print("số nút xe của bạn là:", sonutxe)
else:
    print("không xác định")