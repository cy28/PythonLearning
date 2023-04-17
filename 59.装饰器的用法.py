# 1. 一个装饰器修饰多个函数
# 举例：定义一个装饰器函数，为下面数学运算函数添加解释说明

# 本次装饰器函数
def interpreter(fn):                                    # 定义装饰器的函数名，并传入要修饰的函数
    def inner(*args):                                   # 定义一个内部函数，传入要修饰函数所需要的参数
        print('本次数学运算的结果是：', end=" ")             # 对函数进行修饰
        fn(*args)
    return inner                                        # 返回内层函数


@interpreter
def add(x, y, z):
    print(x + y + z)
   # return x + y + z   变量接得是函数的返回值


@interpreter
def minus(x, y, z):
    print(x - y - z)


add(12, 45, 66)

# 一个函数由多个装饰器函数修饰时，装饰器函数是从下往上调用的，从离原函数最近的装饰器开始调用


def outer1(func):
    def inner1():
        func()
        print('谢谢，我很好')
    return inner1


def outer2(func):
    def inner2():
        func()
        print('现在是什么时候')
    return inner2


@outer2
@outer1
def dialog():
    print('你好吗')


dialog()

# 你好吗
# 谢谢，我很好
# 现在是什么时候


















