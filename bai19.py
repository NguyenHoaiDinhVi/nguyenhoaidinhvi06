# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:19:56 2024

@author: Admin
"""

print("nhập vào 4 số nguyên")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
sonhonhat=a
if b<a:
    sonhonhat=b
elif c<a:
    sonhonhat=c
elif d<a:
    sonhonhat=d
print("số nhỏ nhất trong 4 số là:",sonhonhat)