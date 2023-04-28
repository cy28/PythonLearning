# 写一个函数，传入两个数字，将其中一个较大的值输出

def maxvalue(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)


maxvalue(12, 54)  # 54

"""
注意
1. 定义函数时，传入的参数叫做形式参数，也叫作形参
2. 调用函数时，传入的参数叫做实际参数，也叫作实参
3，形参和实参的名字可以一致，因为本质上他们开辟的是不同的内存
"""





def get_sum(num1, num2, num3=100):
    print(num1+num2+num3)


get_sum(12, 28)  # 140
get_sum(12, 28, 0)  # 40














