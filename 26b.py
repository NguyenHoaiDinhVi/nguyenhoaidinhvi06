# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:22:43 2024

@author: Admin
"""

a=int(input("nhập chũ số thứ nhất:"))
b=int(input("nhập chữ số thứ hai:"))
c=int(input("nhập chữ số thứ ba:"))
d=int(input("nhập chữ số thứ tư:"))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if a>d:
    a,d= d,a
if b>c:
    b,c=c,b
if b>d:
    b,d= d,b
if c>d:
    c,d= d,c
print("các chữ số theo thứ tự tăng dần:",a,b,c,d,sep="")


