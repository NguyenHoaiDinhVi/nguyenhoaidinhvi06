# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:34:47 2024

@author: Admin
"""

a = float(input("Nhập số a= "))
b = float(input("Nhập số b= "))
c = float(input("Nhập số c= "))
if a > b:
    a, b = b, a  
if a>c:
    a, c = c, a
if b>c:
    c, b = b, c  
print("Ba số theo thứ tự tăng dần là: {}, {}, {}".format(a,b,c))
