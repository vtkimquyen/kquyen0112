# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:30:31 2024

@author: Kim Quyên
"""

import random

Người_chơi_chọn = input("Bạn chọn gì?(kéo, búa, bao):")
chọn = ["kéo", "búa", "bao"]
Máy_chọn=random.choice(chọn)

print(f"Bạn chọn {Người_chơi_chọn}, Máy chọn {Máy_chọn}")

if Người_chơi_chọn == Máy_chọn:
    print("Hòa nha")
elif Người_chơi_chọn == "kéo" and Máy_chọn == "bao" or\
     Người_chơi_chọn == "búa" and Máy_chọn == "kéo" or\
     Người_chơi_chọn == "bao" and Máy_chọn == "búa":
      print("Bạn là người chiến thắng")
else:
    print("Bạn thua rùi")