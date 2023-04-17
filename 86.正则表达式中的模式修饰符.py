# 模式修饰符用来修饰我们写的正则表达式，是一个可选参数

# .: 表示匹配除了换行之外的所有的字符  \n 表示换行符

# re.S: 可以使 正则表达式中的 . 匹配到换行符 \n

"""
在正则表达式中，re.S标志表示“点任意匹配模式”（dot-all模式）。
这个标志告诉正则表达式引擎将点号.匹配包括换行符在内的所有字符。
通常情况下，点号.在正则表达式中只会匹配除换行符以外的任意字符。
但是如果启用了re.S标志，它就可以匹配包括换行符在内的所有字符。
"""

# re.I: 可以使正则表达式忽略大小写
"""
在Python的正则表达式中，re.I是一个标志，表示“忽略大小写”（ignore case）。
使用re.I标志后，正则表达式引擎将不区分大小写地匹配字符，这意味着大写和小写字符都会被匹配。
"""


import re

print(re.search('shenzhen.', 'shenzhen9'))  # <re.Match object; span=(0, 9), match='shenzhen9'>

print(re.search('shenzhen.', 'shenzhen\n'))  # None

print(re.search('shenzhen.', 'shenzhen\n', re.S))  # <re.Match object; span=(0, 9), match='shenzhen\n'>


print(re.search('shenzhen[a-z]', 'shenzhenM'))  # None

print(re.search('shenzhen[a-z]', 'shenzhenM', re.I))  # <re.Match object; span=(0, 9), match='shenzhenM'>























