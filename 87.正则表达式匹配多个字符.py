# 匹配多个字符

"""
? 表示前面的字符可以出现0次或者1次
+ 表示前面的字符可以出现1次或者多次
* 表示前面的字符可以出现0次或者多次
{} 表示前面的字符可以出现指定的次数或者次数的范围
{3} 表示前面的字符只能出现3次
{3,6} 表示前面的字符能出现3-6次
{3，} 表示前面的字符至少出现3次

"""

import re

print(re.search('goog?le', 'goole'))        # <re.Match object; span=(0, 5), match='goole'>

print(re.search('goog?le', 'google'))       # <re.Match object; span=(0, 6), match='google'>

print(re.search('goog?le', 'googggle'))     # None


print(re.search('goog+le', 'goole'))        # None

print(re.search('goog+le', 'google'))       # <re.Match object; span=(0, 6), match='google'>

print(re.search('goog+le', 'googggle'))     # <re.Match object; span=(0, 8), match='googggle'>


print(re.search('goog*le', 'goole'))        # <re.Match object; span=(0, 5), match='goole'>

print(re.search('goog*le', 'google'))       # <re.Match object; span=(0, 6), match='google'>

print(re.search('goog*le', 'googggle'))     # <re.Match object; span=(0, 8), match='googggle'>


print(re.search('goog{3}le', 'googggle'))   # <re.Match object; span=(0, 8), match='googggle'>









