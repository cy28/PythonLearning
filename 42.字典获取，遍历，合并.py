# 1. 获取字典的一些参数
dict1 = {'name': '中国医生', 'director': '刘伟强', 'actor': '张涵予', 'address': 'Shanghai'}

# 获取字典的长度
print(len(dict1))  # 4

# 获取字典中所有的key值
print(dict1.keys())  # dict_keys(['name', 'director', 'actor', 'address'])

# 获取字典中所有的value值
print(dict1.values())  # dict_values(['中国医生', '刘伟强', '张涵予', 'Shanghai'])

# 获取字典中所有的键值
print(dict1.items())  # dict_items([('name', '中国医生'), ('director', '刘伟强'), ('actor', '张涵予'), ('address', 'Shanghai')])

# 2. 遍历字典

# 方法一：for in

for key in dict1.keys():
    print(key)
# name
# director
# actor
# address

for value in dict1.values():
    print(value)
# 中国医生
# 刘伟强
# 张涵予
# Shanghai

for k, v in dict1.items():
    print(k, v)
# name 中国医生
# director 刘伟强
# actor 张涵予
# address Shanghai

# 3. 合并字典 update() 里面的参数填要合并的字典
dict2 = {'name': '成龙', 'sex': '男', 'age': '61'}
dict3 = {'region': '香港'}
dict2.update(dict3)
print(dict2)  # {'name': '成龙', 'sex': '男', 'age': '61', 'region': '香港'}







