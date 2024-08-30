# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:32:42 2024

@author: Admin
"""
import math
a=float(input("a="))
b=float(input("b="))
q= math.pow(a,1/3)
w=math.pow(b,1/3)
e=math.pow(a*b,1/3)
bt1=((a+b)/(q+w))-e
bt2=(q-w)**2
bt=bt1/bt2
print("giá trị của biểu thức=",round(bt,3))