# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:28:02 2024

@author: Kim Quyên
"""

distance=float(input("Nhập độ dài đoạn đường đến trường (m):"))
if distance < 300:
    print("Đường đến trường quá gần. Thôi! Đi bộ")
elif distance > 1200:
    print("Đường đến trường quá xa. Thôi! Đi xe máy")
elif distance >= 300 and distance <=700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp")
else:
    print("Không xác định")