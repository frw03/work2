# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle_properties(radius):
    
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    return circumference, area

radius = float(input("請輸入圓的半徑: "))

circumference, area = calculate_circle_properties(radius)

print(f"圓周長: {circumference:.2f}")
print(f"圓面積: {area:.2f}")