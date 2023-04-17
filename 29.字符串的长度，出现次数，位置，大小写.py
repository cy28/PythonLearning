"""
1. 获取字符串长度和统计字符串出现的次数

str1 = "我的电脑卡了，你的电脑卡吗？"

# len() 统计字符串长度
print(len(str1))  # 14

# count() 在整个字符串中统计子串出现的次数
print(str1.count("电脑"))  # 2

"""


"""

2. 字符串中的大小写转换

   upper()      lower()         # 括号里面不需要参数，因为是将整个字符串变为大小写
   swapcase()                   # 将字符串大写变小写，小写变大写
   title()                      # 将英文单词中的每一个首字母，都变成大写
   

str2 = "I Miss you VERY much"
print(str2.upper())     # I MISS YOU VERY MUCH
print(str2.lower())     # i miss you very much
print(str2.swapcase())  # i mISS YOU very MUCH
print(str2.title())     # I Miss You Very Much

"""


"""
3. 查找字符串出现的位置

查找-find() 查找子串在字符串中[第一次]出现的位置，若找到了返回的是下标，若没找到返回的是-1
索引-index() 功能和find类似，区别在于如果其未找到，就直接报错
rfind() 查找子串在字符串中[最后一次]出现的位置，找到了返回的是下标，若未找到返回-1  ----right find 
rindex() 功能和rfind类似，区别在于如果其未找到，就直接报错

注意：可以在指定范围类查找和索引

"""

str3 = "abcdefghijklmn1239876l54zxyslt"

print(str3.find("l"))       # 11 下标还是以0开始，且返回的是第一次出现的位置
print(str3.find("o"))       # -1
print(str3.index("a"))      # 0
# print(str3.index("o"))      # ValueError: substring not found
print(str3.rfind("l"))      # 28
print(str3.rindex("l"))     # 28

# 在限定范围类查找和索引

print(str3.find("l", 3, 12))    # 11  从下标3开始，到下标12，但不包括12
print(str3.index("l", 3, 12))    # 11
print(str3.rfind("l", 12, 30))    # 28
print(str3.rindex("l", 12, 30))    # 28
