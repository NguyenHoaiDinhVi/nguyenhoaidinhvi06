# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:39:57 2024

@author: Admin
"""

print("chọn 1,2,3 theo thứ tự tính chu vi hình chữ nhật, hình vuông, hình tròn")
w=int(input("w="))
if w==1:
    print("tính chu vi và diện tích của hình chữ nhật")
    a=float(input("chiều dài="))
    b=float(input("chiều rộng="))
    cv=2*(a+b)
    dt=a*b
    print("diện tích hình chữ nhật=",round(dt,2))
    print("chu vi hình chữ nhật=",round(cv,2))  
elif w==2:
    print("tính chu vi và diện tích của hình vuông")
    a=float(input("cạnh="))
    cv=a*4
    dt=a*a
    print("diện tích hình vuông=",round(dt,2))
    print("chu vi hình vuông=",round(cv,2))
elif w==3:
    print("tính chu vi và diện tích của hình tròn")
    a=float(input("bán kính="))
    cv=2*a*3.14
    dt=a*a*3.14
    print("diện tích hình tròn=",round(dt,2))
    print("chu vi hình tròn=",round(cv,2)) 