"""
1. 字符串替换   在字符串中对指定内容进行替换
# replace() 对指定数据进行替换
第一个参数:要替换的内容
第二个参数:替换后的内容
第三个参数；替换的次数

举例
str1 = "这个店铺的商品很垃圾，这么垃圾的商品还拿出来卖？"
print(str1)  # 这个店铺的商品很垃圾，这么垃圾的商品还拿出来卖？
print(str1.replace("垃圾", "**"))  # 这个店铺的商品很**，这么**的商品还拿出来卖？
print(str1.replace('垃圾', '**', 1))  # 这个店铺的商品很**，这么垃圾的商品还拿出来卖？

"""

"""
2. 字符串判断  判断字符串是否符合特定的要求
返回的结果是布尔类型 若成立返回True 若不成立 返回FALSE

# isupper()  判断字符串中的字母是否全部是大写
# islower()  判断字符串中的字母是否全部是小写
# isdigit()  判断字符串是否全部是数字
# istitle()  判断字符串的瘦首字母是否大写
# isalpha()  判断字符串中的数字是否全部是由字母或者文字组成

"""

print("helloWORLD".isupper())  # False
print('HELLO'.isupper())  # True
print('hello'.islower())  # True
print('123'.isdigit())    # True
print('123aa0'.isdigit())  # False
print('Hello World'.istitle())  # True
print('你好jack'.isalpha())  # True
print('你好jack123'.isalpha())  # False


