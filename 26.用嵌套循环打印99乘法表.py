"""
总结： 在嵌套循环中， 外层循环执行一次，内层循环执行一圈
"""

"""
举例1： 使用while循环打印9*9乘法表

i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print(j, "*", i, "=", i * j, end="  ")
    print("")
    
"""

# 举例2；使用for循环打印9*9乘法表

for i in range(1, 10):  # 确定行数是1到9行
    for j in range(1, i+1):  # 确定每行输出的个数，是i个
        print(j, "*", i, "=", i*j, end=" ")
    print("")






























