"""
\d: 匹配数字，0-9之间的任意数字
\D: 匹配非数字字符
[^0-9]: 匹配不是0-9的字符，相当于 \D
\w: 匹配数字 字母 下划线，相当于[0-9a-zA-Z_]  且只匹配一次
\W: 匹配非数字 非字母 非下划线，相当于[^0-9a-zA-Z_]  且只匹配一次
\s: 匹配任意空白字符，包括空格、制表符\t、换行符\n、回车\r、换页\f。
\S: 匹配任意非空白字符
[]: 表示匹配括号类的一位
-: 表示一个区间
.: 表示除换行符之外的任意字符
"""
import re

print(re.search('hello\w', 'hello!'))  # None
print(re.search('hello\w', 'helloa'))  # <re.Match object; span=(0, 6), match='helloa'>
print(re.search('hello\w', 'helloaf'))  # <re.Match object; span=(0, 6), match='helloa'>  可以看到只进行了一次匹配
print(re.search('hello\w', 'hello_'))  # <re.Match object; span=(0, 6), match='hello_'>

print(re.search('hello\W', 'hello!'))  # <re.Match object; span=(0, 6), match='hello!'>


































