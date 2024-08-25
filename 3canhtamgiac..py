# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:25:16 2024

@author: Kim Quyên
"""

a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))

if a + b > c and a + c > b and b + c > a:
    print(f"{a}, {b}, {c} là ba cạnh của tam giác")
else:
    print(f"{a}, {b}, {c} không phải là ba cạnh của tam giác")
    