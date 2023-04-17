# random模块主要用于生成随机数或者从一个列表中随机获得数据

import random
# 1. random()：返回一个 0 到 1 之间的随机浮点数。

print(random.random())  # 生成一个 0 到 1 之间的随机浮点数

# 生成一个 0 到 1 之间的随机浮点数
print(random.uniform(1, 3))

# 2. randint(a, b)：返回一个 a 到 b 之间的随机整数。

print(random.randint(1, 100))  # 生成一个 1 到 100 之间的随机整数

# 3. randrange([start], stop[, step])：返回一个从 start（默认为 0）到 stop（不包括）之间，按照 step（默认为 1）递增的随机整数。

print(random.randrange(0, 10, 2))  # 生成一个 0 到 10 之间，按照 2 递增的随机整数

# 4. choice(seq)：从序列 seq 中随机选择一个元素。

list1 = [1, 2, 3, 4, 5]
print(random.choice(list1))  # 随机选择 list1 中的一个元素

# 5. shuffle(seq)：将序列 seq 中的元素随机排序。

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)  # 将 list1 中的元素随机排序
print(list1)

# 6. sample(population, k)：从总体 population 中随机选择 k 个元素。

list1 = [1, 2, 3, 4, 5]
print(random.sample(list1, 3))  # 从 list1 中随机选择 3 个元素
































