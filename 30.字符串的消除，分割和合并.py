"""
1. 消除指定字符串

# strip（）去除字符串两边的指定字符（如果不指定，则默认是去除空格）
# lstrip() 只去除字符串左边的指定字符
# rstrip() 只去除字符串右边的指定字符

举例一 ：

str1 = "    today is a nice day    "
str2 = "****today is a nice day****"
print(str1)                 #    today is a nice day
print(str1.strip())         # today is a nice day
print(str2)                 # ****today is a nice day****
print(str2.strip("*"))      # today is a nice day
print(str2.lstrip("*"))     # today is a nice day****
print(str2.rstrip("*"))     # ****today is a nice day

"""

"""
2. 字符串的合并和分割

# split() 以指定字符对字符串进行分割（默认是空格）
# join()  以指定字符对字符进行拼接

"""

str3 = "this is a string example"

print(str3.split())  # ['this', 'is', 'a', 'string', 'example'] 以空格为分割，切成列表的形式

print(str3.split("i"))  # ['th', 's ', 's a str', 'ng example']

str4 = "-"
tup = ("hello", "every", "body")
print(str4.join(tup))  # hello-every-body 将str4加入到tup
