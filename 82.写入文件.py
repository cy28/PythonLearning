# 1. w模式
# f = open('./TestDoc/example1.txt', 'w') mode = 'w' 会把原来文件中的内容全部替换

# f.write('学到第82级了')

# f.close()

# 2. a模式
f = open('./TestDoc/example1.txt', 'a')         # 'a'已追加的方式向原文添加内容，不会影响原文件的内容

f.write('这是追加的内容')

f.close()


















