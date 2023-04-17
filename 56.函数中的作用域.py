# 作用域：函数能够生效的范围
# 1. 分支语句中变量的作用域
if 5 > 4:
    a = 11
print(a)  # 11  可以看出分支语句中的变量是作用于全局的

# 2. 循环语句中变量的作用域
# a. while 循环
num = 0
while num < 4:
    num += 1
print(num)  # 4

# b. for 循环
for i in range(1, 3):
    b = 3
print(b)  # 3
# 以上可以看出循环语句中的变量也是作用于全局的

# 3.函数  外部访问函数内部报错，但是函数内部可以访问函数外部变量

"""
a. 函数外部访问函数内部变量

def fn():
    c = 10
print(c)  #name 'c' is not defined

"""
# b. 函数内部访问函数外部变量

num = 99


def demo():
    print(num)


demo()  # 99

"""
总结：
    1. 分支语句和循环语句不存在作用域问题，他们里面定义的变量可以在外部直接访问
    2. 函数内部的变量，在函数外部不能直接访问
    3. 函数内部可以直接访问函数外部的变量
"""

# 函数内外部同一名字的变量表达的内容是不一样的
num1 = 66


def fn1():
    num1 = 88
    print(num1)


print(num1)  # 66
fn1()  # 88


# 若想在函数函数内部直接修改函数外部的变量，需要使用global关键字，将函数内部变量变为全局变量

num2 = 66


def fn2():
    global num2
    num2 = 88
    print(num2)


fn2()  # 88
print(num2)  # 88
