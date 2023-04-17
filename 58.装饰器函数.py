"""
装饰器的定义：

1. 装饰器函数是指在Python中用于修改其他函数行为的函数。装饰器函数接受一个函数作为输入，并返回一个新的函数作为输出。
2. 这个新函数可以用来代替原始函数，从而实现对原始函数的行为进行修改、增强或扩展。
3. 装饰器函数的特点是它们本身也是函数，因此可以被调用和传递参数。

"""

# 在Python中，装饰器函数通常使用@语法糖来应用到需要修改行为的函数上。
# 例如，以下代码定义了一个名为my_decorator的装饰器函数，它可以将被装饰函数的输出字符串转换为大写字母：


def my_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@my_decorator
def my_function():
    return "hello, world!"


print(my_function())  # 输出 "HELLO, WORLD!"


"""
在这个例子中，@my_decorator语法糖将my_decorator装饰器应用到my_function函数上，使得my_function函数的输出结果被转换为大写字母。
"""

















