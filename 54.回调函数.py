# 回调函数：把一个函数a作为参数传递给另一个参数b，参数a就叫做回调参数

def add(x, y):
    print(x+y)


def minus(x, y):
    print(x-y)


def multiply(x, y):
    print(x*y)


def divide(x, y):
    print(x/y)


def calculate(x, y, fuc):
    fuc(x, y)


# 加法
calculate(12, 34, add)  # 46

# 乘法
calculate(12, 2, multiply)  # 24










