# python中的集合的概念和数学中的集合概念是相似的

# 特点： 1. 无重复元素的集合，特点是无序的
#       2. 元素类型不一定要保持一致，可以是整数，浮点数，字符串等
#       3. 每个元素是不可变的

# 1. 创建集合
set1 = {12, 34, 5, 67, True}
print(set1)  # {True, 34, 67, 5, 12}  注意 输出的结果是无序的
print(type(set1))  # <class 'set'>

# 2. 集合中的元素不能通过下标进行访问和修改，因为是无序的
# print(set1[1])  'set' object is not subscriptable
# set1[1] = 8  'set' object does not support item assignment

# 3. 获取结合的长度 len()
print(len(set1))  # 5

# 4. 向集合中添加元素

# add() 只能一次添加一个元素
set1.add(66)
print(set1)  # {True, 34, 67, 66, 5, 12}

# update() 一次性向集合添加多个元素 ([   ])   括弧里面以列表的形式添加
set1.update([11, 56, 99])
print(set1)  # {True, 66, 67, 5, 11, 12, 34, 99, 56}

# 5. 删除集合元素

# pop() 随机删除集合中的一个元素
set1.pop()
print(set1)  # {66, 67, 5, 11, 12, 34, 99, 56}

# remove() 删除指定的元素，参数传入指定要删除元素的值，如果传入不存在的值，系统（会）报错
set1.remove(66)
print(set1)  # {67, 5, 11, 12, 34, 99, 56}

# discard()  删除指定的元素，参数传入指定要删除元素的值，如果传入不存在的值，系统（不会）报错
set1.discard(67)
set1.discard(9)
print(set1)  # {5, 11, 12, 34, 99, 56}

# 6. 清空集合
# set1.clear()
# print(set1)  # set()

# 7. 遍历集合
for i in set1:
    print(i)
# 5
# 11
# 12
# 34
# 99
# 56
















