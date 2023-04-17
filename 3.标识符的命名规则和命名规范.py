# 标识符主要是作为变量、函数、类、模块以及其他对象的名称
"""
定义合法标识符的规则：
1. 由数字，字母和下划线组成，不能以数字开头
2. 严格区分大小写
3. 不同够使用python中关键字作为标识符 可以通过keyword模块中的kwlist属性查看有哪些关键字
常见的关键字如下：
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']


"""

import keyword
print(keyword.kwlist)


"""
标识符的命名规范：
1. 见名知意
2. 遵守一定的命名规范
    a. 小驼峰命名法：第一个单词的首字母小写，以后每个单词首字母大写   eg：userNameAndPassword
    b. 大驼峰命名法：每个单词首字母大写   eg：UserName
    c. 下划线命名法：单词之间使用下滑线拼接  eg：user_name
3. 一般变量，函数，模块使用下划线命名法，类名使用大驼峰命名法




"""











