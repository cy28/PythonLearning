"""
python中while循环结构的语法：

初始条件
while 判断条件：
    循环体
    更新条件

注意：
1 在while循环中，初始条件只会在第一次循环中执行，后续的循环不在执行初始条件
2 在python中，没有自增自减运算符
3 在python中，没有do while循环结构

"""

num = 0
while num < 4:
    print("hello!")  # 注意这里要缩进四个空格
    num += 1    # 注意这里也要缩进四个空格

# hello!
# hello!
# hello!
# hello!



