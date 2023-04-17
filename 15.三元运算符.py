# 三元运算符是对if else的简化写法
# 比较大小的if else写法

a = 12
b = 24
"""
if a > b:
    print("大的数字是", a)
else:
    print("大的数字是", b)
"""
# 如果是三元运算符，那么两边是要输出的值，中间是判断的条件，输出的值用一个变量去接
c = a if a > b else b
print("大的数字是：", c)


















