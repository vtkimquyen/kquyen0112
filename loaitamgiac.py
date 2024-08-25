# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:24:32 2024

@author: Kim Quyên
"""

a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))

if (a+b)>c and (b+c)>a and (c+a)>b:
    print("Là 3 cạnh  tam giác")
if c**2==a**2+b**2 or a**2==b**2+c**2 or b**2==a**2+c**2:
    print("Là 3 cạnh tam giác vuông")
elif a==b !=c or a==c !=b or b==c !=a:
    print("Là 3 cạnh tam giác cân")
elif a==b==c:
    print("Là 3 cạnh tam giác đều")
else:
    print("Là 3 cạnh tam giác thường")