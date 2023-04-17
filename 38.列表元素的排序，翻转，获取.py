# 排序

"""
# 1. sort()  对原列表中的元素进行排序，默认是升序，不会生成新列表

list1 = [12, 34, 21, 35, 6, 24]

list1.sort()  # 不传入参数，则默认是升序排列
print(list1)  # [6, 12, 21, 24, 34, 35]

list1.sort(reverse=True)  # 若想实现降序排列，则传入参数revere=True
print(list1)  # [35, 34, 24, 21, 12, 6]

"""

# 2. sorted() 会把排序后的结果生成一个新列表，传入的参数是原列表

list1 = [12, 34, 21, 35, 6, 24]

list2 = sorted(list1)  # 默认是升序排列
print(list2)  # [6, 12, 21, 24, 34, 35]

list2 = sorted(list1, reverse=True)  # 传入参数，降序排列
print(list2)  # [35, 34, 24, 21, 12, 6]

#  3. sorted() 还可以传入参数关键字，根据参数关键字进行排序

list3 = ['abc', 'mm', 'd', 'hello', 'word']
list4 = sorted(list3, key=len)
print(list4)  # ['d', 'mm', 'abc', 'word', 'hello']

#  4. reverse() 翻转列表 最后的元素变第一个，然后依次翻转

list5 = [23, 3345, 67,  89, 21]
list5.reverse()
print(list5)  # [21, 89, 67, 3345, 23]

#  5. 获取列表长度len() 传入的参数是列表
# 总结：一般如果是对列表进行操作，就是list.
# 如果要获得一个什么东西，就把列表传进当参数

list6 = [52, 34, 128, True, 'hello']
print(len(list6))  # 5


# 6. 获取列表中的最大和最小值 max() min() 针对列表中全是数字的情况

list7 = [32, 43, 5445, 65, 789, 43]
print(max(list7))  # 5445
print(min(list7))  # 32

# 7. 获取指定元素的索引  index()传入的参数是要进行索引的元素

print(list7.index(5445))  # 2



