import re

"""
1. re.split 是 Python 中 re 模块提供的一个函数，用于按照指定的正则表达式模式分割字符串。函数定义如下：

re.split(pattern, string, maxsplit=0, flags=0)

其中，参数 pattern 表示正则表达式模式，
参数 string 表示要被分割的字符串，
maxsplit 表示最多分割次数（默认为0，即分割所有匹配项），
flags 表示正则表达式的匹配模式。

"""


import re

s = "Hello, world! This is a test."
parts = re.split(",\s+", s)

print(parts)  # ['Hello', 'world! This is a test.']


"""
在这个例子中，我们首先导入了 re 模块，然后定义了一个字符串 s。
我们使用 re.split 函数将 s 按照逗号和一个或多个空格进行分割，并将结果存储在 parts 变量中。
最后，我们打印了 parts 变量的值，结果为 ['Hello', 'world! This is a test.']。
这个例子中的正则表达式模式 ",\s+" 表示一个逗号后面跟着一个或多个空格。
因此，字符串中所有符合这个模式的地方都会被用来分割字符串。

"""

"""
2. re.sub 是 Python 中 re 模块提供的一个函数，用于根据指定的正则表达式模式，将字符串中的匹配项替换成指定的字符串或函数返回值。函数定义如下：

re.sub(pattern, repl, string, count=0, flags=0)

其中，参数 pattern 表示正则表达式模式，
参数 repl 表示替换成的字符串或函数，
参数 string 表示要被替换的字符串，
count 表示最多替换次数（默认为0，即替换所有匹配项），
flags 表示正则表达式的匹配模式。

"""

s = "I have 3 apples and 5 oranges."
s = re.sub(r"\d+", "NUMBER", s)

print(s)  # 'I have NUMBER apples and NUMBER oranges.'

"""
在这个例子中，我们首先导入了 re 模块，然后定义了一个字符串 s。
我们使用 re.sub 函数将 s 中的所有数字替换成字符串 "NUMBER"，并将结果存储回 s 变量中。
最后，我们打印了 s 变量的值，结果为 'I have NUMBER apples and NUMBER oranges.'。
"""

















