# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:43:40 2024

@author: Admin
"""

a=int(input("giờ:"))
b=int(input("phút:"))
c=int(input("giây:"))
w=(a*3600)+(b*60)+c
print("thời gian:{}:{}:{}".format(a,b,c))
print("số giây là:",w)