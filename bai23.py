# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:29:52 2024

@author: Admin
"""

print("giải phương trình bậc hai a*x**2 +bx+c=0")
a=float(input("nhập giá trị của a:"))
b=float(input("nhập giá trị của b:"))
c=float(input("nhập giá trị của c:"))
if a==0:
    x=-c/b
    print("nghiệm của phương trình là:",x)
if a!=0:
    delta= b**2- (4*a*c)
    if delta<0:
        print("phương trình vô nghiệm")
    elif delta==0:
        print("phương trình có một nghiệm kép")
        print("x1=x2=",-b/2*a)
    elif delta>0:
        print("phương trình có 2 nghiệm")
        import math
        print("x1 = ", (-(b) + math.sqrt(delta))/(2*a))
        print("x2 = ", (-(b) - math.sqrt(delta))/(2*a))
    else:
        print("không xác định được")