"""
1. 字符串的声明：一对单引号或者一对双引号
              一个三队单引号
              都能声明一个字符串

a = 'hello'
b = "world"
d = '''haha'''
print(a, b, c, d)  # 输出 hello world hello haha 默认间隔为一个空格

2. 若字符串的内容还需要引号包裹，外面是单引号，里面是双引号
                           外面是双引号，里面是单引号
                           
举例
n = "我说’早上好‘"
print(n)  # 输出 我说’早上好‘


3. 转义字符  使得字符失去其原有的意义或者使其具有新的意义

举例

e = "你\"好吗"
print(e)  # 你"好吗

f = "欢迎学习\npython"  # \n  n-new line  换行
print(f)  # 欢迎学习
          # python

g = "今天天气\t很晴朗"  # \t    t-tap 制表符 表示四个空格
print(g)  # 今天天气	很晴朗

"""

"""
4. 一些特殊的字符
   字符串前面加r，表示原样输出   r-raw
   字符串前面加f，支持花括号语法

"""

h = r" i am a \teacher"
print(h)  # i am a \teacher    相当于去掉转义字符造成的影响

name = "cy"
age = "23"
print("我的名字是：", name, "我的年龄是：", age)  # 我的名字是： cy 我的年龄是： 23
print(f"我的名字是：{name} 我的年龄是：{age}")   # 我的名字是：cy 我的年龄是：23




