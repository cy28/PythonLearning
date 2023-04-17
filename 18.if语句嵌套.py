# 在if语句可以再写if语句或者if-else语句
"""
举例
比如我们去火车站乘火车，先要买票，然后过安检，然后检票等一系列流程，一一满足后，才能完成最后的乘车。
"""

ticket = input("请问你是否有车票？（输入yes/no）：")
if ticket == "yes":
    print("请进站")
    safety = input("请问你是否通过安检？（输入yes/no）：")
    if safety == "yes":
        print("请上车")
    else:
        print("由于你未能通过安检，你不能上车")
else:
    print("由于你没有车票，你不能进站")


















