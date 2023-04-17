# 匿名函数是一个表达式，比普通函数简单，使用lambda表达式


# 匿名函数的语法如下：
# lambda arguments: expression


# 其中，arguments 是匿名函数的参数列表，用逗号分隔。在上面的示例中，参数列表只有一个参数 x。
# expression 是匿名函数的返回值。在上面的示例中，返回值是 x * 2。
# 需要注意的是，匿名函数通常用于只需要执行一次的简单函数，如果需要创建复杂的函数，还是应该使用常规函数定义来进行编写。

def fn(num):
    return num ** 2


num1 = fn(3)
print(num1)  # 9


# 匿名函数实现求一个数字的平方

num2 = lambda num: num ** 2
print(num2(3))  # 9















