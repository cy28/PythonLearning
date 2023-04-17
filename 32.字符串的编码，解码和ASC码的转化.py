"""
字符串的编码和解码

encode()对文字进行编码
主要有两种 gbk和 utf8  字符集
编码 就是将所有的符号全部转化为二进制数
括号里的参数可以填编码的字符集

"""
str1 = '我爱你中国'
print(str1.encode())  # b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd' 默认使用utf-8字符集
print(str1.encode('gbk'))  # b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'

str2 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd'
print(str2.decode())  # 我爱你中国

"""
ASCII码的转化
# chr() 将ASCII码值转化为对应的字符        character 字符
# ord()  获取一个字符对应的ASCII码值       ordinal 序数
"""
print(chr(97))  # a
print(ord('d'))  # 100








