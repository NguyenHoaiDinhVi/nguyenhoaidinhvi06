# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:13:33 2024

@author: Admin
"""

a=int(input("ngày:"))
b=int(input("tháng:"))
c=int(input("năm:"))
#a
print("{}/{}/{}".format(a,b,c))
#b
e=c%100
print(f"{a}/{b}/{e:02d}")
#c
print("{}/{}/{}".format(c,b,a))