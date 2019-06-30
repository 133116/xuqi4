# -*- coding: UTF-8 -*-

# Filename : 05-if.py
# author by : （学员xuqi)

# 目的:
# 掌握使用 if 语句

# 输出指定范围内的素数
# take input from the user
print("-----华丽分割线-----")
print("输出指定范围内所有整数：")
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
for num in range(lower, upper + 1):
    print(num)
