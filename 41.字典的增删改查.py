"""
在使用列表存储多个数据的时候，在获取和修改数据时，会存在一些缺陷。这个时候引出字典来解决这个问题
字典的语法：
dict1 = {key:value, key:value, key:value}

"""

dict1 = {"name": "张三", "age": "32", "height": 175, "sex": "男", "school": "清华大学", "job": "算法工程师"}
print(dict1)

# 1. 访问字典中元素
# 根据索引访问字典中的value值  []中填入要访问的索引值
print(dict1['name'])  # 张三

# 也可以通过get() 来访问， 参数同样是key值, 如果访问的时候没有对应的key值，则返回的值为None
print(dict1.get('job'))  # 算法工程师
print(dict1.get('money'))  # None

# 2. 修改字典中的元素
dict1['name'] = '王五'
print(dict1)  # {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'school': '清华大学', 'job': '算法工程师'}

# 3. 字典中添加元素
dict1['money'] = '55555'
print(dict1)
# {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'school': '清华大学', 'job': '算法工程师', 'money': '55555'}

# 字典中删除元素
# 第一种 pop('要删除元素的key‘)  弹出
dict1.pop('school')
print(dict1)  # {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'job': '算法工程师', 'money': '55555'}

# 第二种 popitem  默认从后往前弹出一个键值
dict1.popitem()
print(dict1)  # {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'job': '算法工程师'}

# 第三种 clear() 表示清空字典
dict1.clear()
print(dict1)  # {}
















