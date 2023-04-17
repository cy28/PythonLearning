"""
练习一
请输出从0到100之间的所有数字

num = 1
while num <= 100:
    print(num)
    num += 1

"""


"""
练习二
输出1-100之间所有数字的和

num = 1
result = 0

while num <= 100:
    result = result + num
    num += 1
print("和为:", result)

"""


"""
练习三
计算1-100之间所有偶数的和

num = 1
result = 0
while num <= 100:
    if num % 2 == 0:     # 判断数字是否为偶数
        result = result + num
    num += 1
print(result)

"""


"""
练习四
计算1-100之间所有奇数的和
"""
num = 1
result = 0
while num <= 100:
    if num % 2 != 0:  # 判断是否为奇数
        result = result + num
    num += 1
print(result)








