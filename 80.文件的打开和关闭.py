# 在Python中，我们使用内置的open()函数来打开文件并读取或写入数据。该函数的语法如下：

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

"""
参数说明：

1. file：要打开的文件名（包括路径）或文件对象。
2. mode：打开文件的模式，如下：
'r'：只读模式（默认值）。
'w'：写入模式，每次写入前会清空文件。
'a'：追加模式，不清空文件，在文件末尾添加新内容。
'x'：独占创建模式，只有文件不存在时才会创建文件，否则会抛出异常。
'b'：二进制模式，与其他模式结合使用，如'rb'，'wb'，'ab'，'xb'等。
't'：文本模式（默认值），与其他模式结合使用，如'rt'，'wt'，'at'，'xt'等。

"""

# 例如，要打开一个名为example.txt的文件以写入模式，可以使用以下代码：


f = open('TestDoc/example.txt', 'w')
# 在完成对文件的操作后，需要使用close()方法关闭文件，以便释放资源和保存数据：

f.write('nihao, shijie')

f.close()
# 另外，为了确保文件在使用后总是被关闭，也可以使用with语句打开文件，当with块结束时，文件会自动关闭：


# with open('example.txt', 'w') as f:
#    f.write('Hello, world!')






























