# 导入math模块：

import math
# 常用的数学函数：

# 1. 平方根：sqrt()  square root

math.sqrt(16)   # 返回4.0

# 2. 绝对值：fabs()

"""
在 C 语言标准库中，fabs() 函数名表示“Floating-point Absolute Value”，
也就是浮点数的绝对值。函数名中的每个字母都对应了这个意思：
f：代表“浮点数”（floating-point）；
abs：代表“绝对值”（absolute value）。
因此，fabs() 函数可以看作是“浮点数的绝对值”函数的缩写。

"""

math.fabs(-1.23)  # 返回1.23

# 3. 向上取整：ceil()

math.ceil(4.1)   # 返回5

# 4. 向下取整：floor()

math.floor(4.9)   # 返回4

# 5. 四舍五入：round()

round(math.pi, 2)   # 返回3.14

# 6. 幂运算：pow()  pow 是 power 的缩写，表示“幂”的意思，也就是计算某个数的某次幂的函数。

math.pow(2, 3)   # 返回8.0

# 7. 对数：log()

math.log(10)   # 返回2.302585092994046

# 8. 三角函数：sin(), cos(), tan()

math.sin(math.pi / 2)   # 返回1.0
math.cos(math.pi)   # 返回-1.0
math.tan(math.pi / 4)   # 返回0.9999999999999999

# 9. 弧度与角度的转换：degrees(), radians()

math.degrees(math.pi / 2)   # 返回90.0
math.radians(90)   # 返回1.5707963267948966

# 10. 常数：
# 圆周率：math.pi

math.pi   # 返回3.141592653589793

# 自然常数：math.e

math.e   # 返回2.718281828459045

# 11. 使用factorial函数计算阶乘：

n = 5
result = math.factorial(n)
print(result)  # 输出120





























