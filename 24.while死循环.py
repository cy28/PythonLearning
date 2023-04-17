"""
死循环 无法终止的循环

举例 输入用户名和密码 只用当用户名和密码正确的时候 才停止输入 否则就一直输入

正确的用户名和密码： 张三  123456
"""

while True:     # 注意python中的真和假T和F都是大写的
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    if username == "张三" and password == "123456":
        print("输入正确，欢迎")
        break  # 当输入正确的时候，要跳出循环，因此要用break终止循环
    else:
        print("输入错误，请重试")









