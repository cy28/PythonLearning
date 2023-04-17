"""
模块：
1. 一个py文件就可以理解为一个模块
2. 但并不是所有的py文件都可以导入使用，必须遵循命名规则
3. python 为了方便开发，提供了很多的内置模块
4. 常见的内置模块有：os sys re math random datetime time calender hashlib uuid hmac

"""

# 1. 第一种：直接使用import关键字导入模块
# 导入模块后，可以使用该模块下的所有的方法和变量
import time
print(time.time())  # 1681266729.3534029

# 2. 第二种：from 模块名 import 方法名或者变量名（这样写的好处在于不用写模块名，可以直接使用方法和变量）

from random import randint

print(randint(1, 10))  # 生成1-10之间的随机整数

# 3. 第三种：from 模块名 import *   # 此处的*表示该模块下所有的变量名和方法名

# 4. 给模块取别名 import 模块名 as 别名

# 5. 给方法名或变量名起别名 from 模块名 import 方法名或者变量名 as 别名

















