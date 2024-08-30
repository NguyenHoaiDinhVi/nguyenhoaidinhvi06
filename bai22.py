# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:28:53 2024

@author: Admin
"""

print("giải phương trình bậc nhất ax+b=0")
a=float(input("nhập giá trị của a:"))
b=float(input("nhập giá trị của b:"))
if a==0 and b==0:
    print("phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("phương trình vô nghiệm")
elif a!=0:
    print("phương trình có nghiệm x=",-b/a)
else:
    print("không xác định được")