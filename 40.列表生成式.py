# 1. 生成1-10之间所有的整数
list1 = list(range(1,11))
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. 得到下列列表[1, 4, 9, 16, 25]

# 法一：通过for循环的方式得到下列列表，通过向空表中一个一个追加完成

list2 = []
for i in range(1,6):
    list2.append(i ** 2)
print(list2)  # [1, 4, 9, 16, 25]

# 法二： 使用列表生成式
# 使用for得到一个i（限制条件也在for循环中），得到i之后，把对i的操作放在for循环之前
# 把对参数i的操作直接放在for的前面


list3 = [i ** 2 for i in range(1, 6)]
print(list3)  # [1, 4, 9, 16, 25]


# 练习1 生成1-10中所有的奇数

list4 = [i for i in range(1, 11) if i % 2 != 0]
print(list4)  # [1, 3, 5, 7, 9]

# 练习2 生成1-10中所有的奇数，且可以被3整除

list5 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 == 0]
print(list5)  # [3, 9]





