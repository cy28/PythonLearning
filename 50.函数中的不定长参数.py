# 不定长参数

# 1. *args：用来接收多个位置的参数，得到一个元组  arguments
def demo(*args):
    print(args)


demo('asd', 12, 34, 789)  # ('asd', 12, 34, 789)

# 定义函数时，若函数中有多个参数，其中某一个参数是不定长参数，一般把不定长参数放在参数列表的最后面


def test(name, *args):
    print(name, args)   # a (123, 456, 'hh', 'hjk')
    print(name, *args)  # a 123 456 hh hjk


test('a', 123, 456, 'hh', 'hjk')


# 2. **kwargs：用来接收多个关键字参数，得到一个字典，在传输参数时，以key=value的形式传输
#   key words arguments

def fn(**kwargs):
    print(kwargs)


fn(x=12, y=13, z='haha')  # {'x': 12, 'y': 13, 'z': 'haha'}







