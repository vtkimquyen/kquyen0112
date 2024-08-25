# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:36:50 2024

@author: Kim Quyên
"""

km=float(input("Số Km quãng đường đi được:"))
if km <= 3:
    if km > 1:
        x = km*13
        print(f"Số tiền phải trả là {x}K")
    else:   
        print("Số tiền phải trả là 20K")
    
else:
    if km <= 8:
       x = 39 + (km - 3)*12
       print(f"Số tiền phải trả là {x}K")
    else:
       x = 39 + 5*12 + (km - 8)*10
       if x > 100:
           a = x*0.92
           print(f"Số tiền phải trả là {a}K")
       else:
           a = x
           print(f"Số tiền phải trả là {a}K")