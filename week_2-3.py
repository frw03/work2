# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:35:04 2024

@author: student
"""

user_input = input("請輸入一個整數: ")

number = int(user_input)

if number % 2 == 0:
    print(f"{number} 是偶數。")
else:
    print(f"{number} 不是偶數。")