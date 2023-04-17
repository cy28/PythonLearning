"""
问题引入：
给一个年龄的列表，想从中得到年龄大于30岁的子表

"""
ages = [12, 34, 56, 77, 89, 43, 25, 32]
"""
法一：通过循环遍历的方式解决

list1 = []
for i in ages:
    if i > 30:
        list1.append(i)
print(list1)  # [34, 56, 77, 89, 43, 32]

"""
# 法二：通过filter的方法

"""
1. filter是一个内置类
2. filter() 内置类有两个参数，第一个参数是一个函数，第二个参数是一个可以迭代的对象
3. 返回值是一个迭代器

"""

list2 = filter(lambda j: j > 30, ages)
print(list2)  # <filter object at 0x000001F6CEA36FE0>
print(list(list2))   # [34, 56, 77, 89, 43, 32]

"""
filter()函数通过使用一个函数来过滤可迭代对象中的元素，仅保留满足特定条件的元素，并返回一个迭代器对象。过滤条件由传递给filter()函数的函数参数决定。

map()函数将可迭代对象中的每个元素传递给一个函数，并返回一个包含函数返回值的新迭代器对象。

因此，filter()函数过滤掉不需要的元素，而map()函数对可迭代对象的每个元素执行一个操作，并返回一个新的可迭代对象。

"""

# filter()函数示例  过滤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(number):
    return number % 2 == 0


even_numbers = list(filter(is_even, numbers))
print(even_numbers)   # 输出 [2, 4, 6, 8, 10]


# map()函数示例  映射
def square(number):
    return number ** 2


squared_numbers = list(map(square, numbers))
print(squared_numbers)   # 输出 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]










