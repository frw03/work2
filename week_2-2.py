# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:22:15 2024

@author: student
"""

def collect_user_data():
    name = input("請輸入您的姓名: ")
    age = int(input("請輸入您的年齡: "))
    height = float(input("請輸入您的身高（米）: "))
    favorite_color = input("請輸入您喜愛的顏色: ")
    
    user_data = {
        '姓名': name,
        '年齡': age,
        '身高': height,
        '喜愛的顏色': favorite_color
    }
    
    return user_data

def format_user_summary(user_data):
    summary = f"{user_data['姓名']}, {user_data['年齡']}歲, 身高{user_data['身高']}米, 喜愛的顏色是{user_data['喜愛的顏色']}。"
    return summary

user_data = collect_user_data()

summary = format_user_summary(user_data)
print(summary)