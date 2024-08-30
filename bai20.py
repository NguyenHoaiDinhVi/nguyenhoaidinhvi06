# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:22:28 2024

@author: Admin
"""

print("nhập vào 3 số")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
solonnhat=a
if b>a:
    solonnhat=b
    print("số lớn nhất là:",solonnhat)
elif c>b:
    solonnhat=c
    print("số lớn nhất là:",solonnhat)
else:
    print("số lớn nhất là:",a)
