"""
time模块是Python标准库中的一个模块，主要用于获取和处理时间。
通过time模块，我们可以获取当前的时间、计算时间间隔、格式化时间等。

下面是一些常用的time模块函数：

time.time(): 返回当前时间的时间戳，即从1970年1月1日零时零分零秒起到现在的秒数。
time.localtime([secs]): 将一个时间戳转换为本地时间，如果不传入参数则返回当前时间。
time.sleep(secs): 让程序休眠secs秒。
time.strftime(format[, t]): 格式化时间，将时间格式化成指定格式的字符串。第二个参数t是可选的，如果不传入则默认使用本地时间。
time.strptime(string[, format]): 将一个字符串解析为时间元组，第二个参数format是可选的，如果不传入则默认使用"%a %b %d %H:%M:%S %Y"格式。
除了上述常用函数外，time模块还有其他一些函数，如：

time.gmtime([secs]): 将一个时间戳转换为UTC时间。
time.asctime([t]): 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2018"（格式化后的）时间字符串。
time.ctime([secs]): 接受时间戳并返回一个可读的形式为"Tue Dec 11 18:07:14 2018"（格式化后的）时间字符串。
time.perf_counter(): 返回一个CPU级别的精确时间计数值，用于性能测试。

"""

import time

# 获取当前时间戳
timestamp = time.time()
print("当前时间戳为：", timestamp)   # 当前时间戳为： 1657651467.6840398

# 将时间戳转换为本地时间元组
local_time = time.localtime(timestamp)
print("本地时间为：", local_time)

# 休眠5秒
print("开始休眠")
time.sleep(5)
print("休眠结束")

# 将时间元组格式化成字符串
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("格式化后的时间为：", formatted_time)   # 格式化后的时间为： 2022-07-12 17:17:47

# 将字符串解析为时间元组
time_str = "2023-04-12 10:30:00"
parsed_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("解析后的时间为：", parsed_time)




