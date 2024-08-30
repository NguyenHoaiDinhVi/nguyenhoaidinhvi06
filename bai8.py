# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:47:07 2024

@author: Admin
"""

print("tính BMI của bạn")
a=float(input("cân nặng(kg):"))
b=float(input("chiều cao(m):"))
bmi=a/b**2
if bmi<16:
    print("gầy độ 3")
elif 16<=bmi<17:
    print("gầy độ 2")
elif 17<bmi<18.5:
    print("gầy độ 1")
elif 18.5<=bmi<25:
    print("bình thường")
elif 25<=bmi<30:
    print("thừa cân")
elif 30<=bmi<35:
    print("béo phì độ 1")
elif 18.5<=bmi<25:
    print("béo phì độ 2")
else:
    print("béo phì độ 3")
