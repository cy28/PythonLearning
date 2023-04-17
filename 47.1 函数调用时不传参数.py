# 如果你调用一个Python函数但没有传递任何参数，那么这个函数将会使用默认参数（如果定义了默认值），
# 或者抛出一个TypeError异常（如果没有定义默认参数且函数要求参数）。
# 具体来说，函数的行为取决于函数定义时的参数情况。
# 如果函数定义时有默认参数，则调用函数时不传递参数时，函数将使用默认值作为参数。例如：

def greet(name="World"):
    print("Hello, " + name + "!")


greet()  # 输出 "Hello, World!"


# 另一方面，如果函数定义时没有默认参数，那么调用该函数时必须传递正确数量的参数，否则会抛出一个 TypeError 异常。例如：

def add_numbers(a, b):
    return a + b


result = add_numbers() # 抛出 TypeError 异常，因为参数数量不正确





































