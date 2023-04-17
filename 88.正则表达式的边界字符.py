# 边界字符

"""
^ : 行首匹配，以指定字符开头
$ : 行位匹配，以指定字符结尾
^文本$ : 文本匹配
"""


# ^：匹配字符串的开头。
# $：匹配字符串的结尾。
# \b：匹配单词边界（即单词与非单词字符之间的位置）。
# \B：匹配非单词边界（即两个单词字符之间的位置）。

# 在Python中，r是一种特殊的字符串前缀，表示原始字符串（raw string）。使用r前缀的字符串中的反斜杠（\）不会被解释为转义字符，而是直接表示为反斜杠本身。


import re


# 匹配以a开头的字符串
pattern = "^a.*"
print(re.match(pattern, "apple"))  # 匹配成功，输出 <re.Match object; span=(0, 5), match='apple'>
print(re.match(pattern, "banana"))  # 匹配失败，输出 None

# 匹配以ing结尾的字符串
pattern1 = ".*ing$"
print(re.match(pattern1, "running"))  # 匹配成功，输出 <re.Match object; span=(0, 7), match='running'>
print(re.match(pattern1, "jumping"))  # 匹配成功，输出 <re.Match object; span=(0, 7), match='jumping'>

# 匹配包含单词"cat"的字符串
pattern2 = r"\bcat\b"
print(re.search(pattern2, "The cat is black"))  # 匹配成功，输出 <re.Match object; span=(4, 7), match='cat'>
print(re.search(pattern2, "The category is animals"))  # 匹配失败，输出 None

# 匹配不包含单词"cat"的字符串
pattern3 = r"\Bcat\B"
print(re.search(pattern3, "The category is animals"))  # 匹配失败，输出 None
print(re.search(pattern3, "The cat is black"))  # 匹配失败，输出 None



















