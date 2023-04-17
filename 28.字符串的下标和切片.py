"""
下标：也叫索引，表示字符串中的第几个数据
下标一般从零开始，可以通过下标获得指定位置的数据

str1 = "welcome"
print(str1[3])  # c

"""

"""
切片：从字符串中复制一段指定内容，生成一个新的字符串

切片的语法：
    字符串[start:end:step]
    start 表示开始下标，包含该下标对应的值
    end 表示结束下标，不包含改下标对应的值
    step 表示截取的步长，默认值为1
    
"""

str2 = "welcome"
print(str2[0:3])        # wel      012           包含start，不包含end
print(str2[1:])         # elcome   123456        从start开始，一直截取到结束
print(str2[:4])         # welc     0123          从开始一直截取到结束
print(str2[1:4:2])      # ec       13            从1开始，隔两个步长截取
# print(str2[1:4:0])     # ValueError: slice step cannot be zero 步长不能为0
print(str2[::])         # welcome        如果所有参数都不指定，则表示截取整个字符串
print(str2[::-1])       # emoclew        表示翻转字符串
print(str2[-3:-1])      # om 都是负数就是从右往左数 最右边的数字下标为0













