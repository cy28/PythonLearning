# python中 = 表示把右边的值赋给左边的变量

num = 13
print(num + 12)

num = num + 14  # 将num中的值加14之后，再赋值给num
print(num)

num += 13   # 等价于 num = num + 13 相当于指明了运算符和操作数，对赋值运算进行了一次简写
print(num)

num1 = 3
num1 **= 2  # **表示进行幂运算，这里相当于进行平方运算
print(num1)

# 注意python中没有++ 和--的运算
# 只能写成 num +=1 或者num -=1
