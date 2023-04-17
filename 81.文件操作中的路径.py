"""
路径分为两种:

1.  绝对路径：从电脑的盘符开始的路径 比如 E:\Code-Learning\SpiderLearning\text1.txt
    但是‘\’在python中表示转义字符，于是改成 E:/Code-Learning/SpiderLearning/text1.txt

2.  从当前执行文件所在的文件夹开始的路径
    . 表示当前目录（当前执行文件所在的文件夹）
    .. 表示上一级目录
    ../../ 上上级目录

"""

# 绝对路径演示
"""
f = open('E:/Code-Learning/SpiderLearning/text1.txt', 'r')

print(f.read())

f.close()
"""
# 相对路径演示  当前目录指的是PythonLearning
f1 = open('./TestDoc/example.txt', 'r')

print(f1.read())

f1.close()




















