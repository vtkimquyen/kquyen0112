# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:31:42 2024

@author: Kim Quyên
"""

import sys
tgian = input("Nhập vào ngày tháng năm theo định dạng dd/mm/yyyy hoặc dd-mm-yyyy : ")
if '/' in tgian:
    dd, mm, yyyy = map(int, tgian.split('/'))
elif '-' in tgian:
    dd, mm, yyyy = map(int, tgian.split('-'))
else:
    print("Sai định dạng!")
    sys.exit()
    
nam_nhuan = (yyyy % 4 == 0 and yyyy % 100 != 0) or yyyy % 400 == 0
so_ngay_trong_thang = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if mm < 1 or mm > 12:
    print(f"{dd:02d}/{mm:02d}/{yyyy} không hợp lệ")
    sys.exit()
elif mm == 2:
    if nam_nhuan:
        ngay_toi_da = 29
    else:
        ngay_toi_da = 28
else:
    ngay_toi_da = so_ngay_trong_thang.get(mm)
    
if 1 <= dd <= ngay_toi_da:
    print(f"{dd:02d}/{mm:02d}/{yyyy} là ngày hợp lệ")
else:
    print(f"{dd:02d}/{mm:02d}/{yyyy} là ngày không hợp lệ")