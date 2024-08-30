# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:30:26 2024

@author: Admin
"""

print("nhập thời gian")
a=int(input("giờ="))
b=int(input("phút="))
c=int(input("giây="))
if 0<=a<24 and 0<=b<=60 and 0<=c<=60:
    print("thời gian hợp lệ:{}:{}:{}".format(a,b,c))
else:
    print("thời gian không hợp lệ")