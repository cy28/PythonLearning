# 1. 合并列表

list1 = [12, 445, 6, 4, 53]
list2 = ['东航', '马虎', '听话']
print(list1 + list2)

# 2. 判断指定元素是否在列表中   通过in 和 not in 进行判断 返回True和False

list3 = ['hello', 'world', '你好', '呵呵', 124, 56]
print('呵呵' in list3)  # True
print('哈哈' in list3)  # False

# 列表的切片
print(list3[1:4])  # ['world', '你好', '呵呵']
print(list3[:4])   # ['hello', 'world', '你好', '呵呵']
print(list3[1:])   # ['world', '你好', '呵呵', 124, 56]
print(list3[-3:])  # ['呵呵', 124, 56]  负数就是从右往左看

























