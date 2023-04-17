# 假设我们有一个函数 multiply(a, b)，它可以计算两个数的乘积。
# 现在我们想要给这个函数添加一个装饰器，使得每次调用函数时都会输出函数的运行时间。
# 我们可以使用闭包函数来实现这个装饰器。

import time


def timer_decorator(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"函数 {func.__name__} 运行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper


@timer_decorator
def multiply(a, b):
    time.sleep(1)
    return a * b


result = multiply(3, 4)

print(result)

"""
在这个例子中，我们定义了一个装饰器函数 timer_decorator，它接受一个函数作为参数并返回一个新的闭包函数 wrapper。

在 wrapper 函数内部，我们首先记录函数运行的起始时间，然后调用原函数 func 并获取其返回值。

接着，我们记录函数运行的结束时间，并输出函数的运行时间。最后，我们将原函数的返回值作为闭包函数 wrapper 的返回值。

我们使用 @timer_decorator 将装饰器应用到 multiply 函数上。这相当于执行了以下代码：

"""

multiply = timer_decorator(multiply)

"""
这将 multiply 函数替换为一个新的函数，即闭包函数 wrapper。

当我们调用 multiply(3, 4) 时，实际上是在调用 wrapper(3, 4)，这个函数内部包含了计时器的逻辑。

最后，我们将 multiply 函数的返回值打印出来，即 12。

通过使用闭包函数，我们可以将装饰器函数作为一个闭包嵌套在原函数内部，从而实现了对原函数的装饰。

这种方式使得装饰器函数可以访问原函数的变量和参数，并在函数调用前后执行一些额外的操作，例如计时、日志记录等。
"""







































