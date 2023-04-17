"""
练习一
任意输入一个数字，判断是否大于16，若大于16输出该数字大于16，否则不输出

num = int(input("请输入一个数字："))
if num > 16:
    print(num, "大于16")
"""


"""
练习二
任意输入一个数字，判断是奇数还是偶数

num1 = int(input("请输入一个数字:"))
if num1 % 2 == 0:
    print(num1, "是偶数")
else:
    print(num1, "是奇数")
"""


"""
练习三
分别输入年月日三个值，然后判断这一天是一年的第几天，考虑闰年和平年的情况
"""
year = int(input("输入的年份为："))
month = int(input("输入的月份为："))
day = int(input("输入的天为："))

# 现在定义一个变量来表示天数加和的值
# 需要注意的是闰年和平年只对一年的二月份造成影响，所以我们只要在二月份放一个选择语句即可
days = day
if month > 1:
    days += 31
if month > 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days += 29
    else:
        days += 28
if month > 3:
    days += 31
if month > 4:
    days += 30
if month > 5:
    days += 31
if month > 6:
    days += 30
if month > 7:
    days += 31
if month > 8:
    days += 31
if month > 9:
    days += 30
if month > 10:
    days += 31
if month > 11:
    days += 30
print("所输入的日期在该年的第", days,"天")














