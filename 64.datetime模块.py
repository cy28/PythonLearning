"""
datetime模块是Python标准库中的一个日期和时间处理模块，提供了许多有用的函数和类来操作日期和时间。

该模块中最重要的类是datetime类，它可以表示日期和时间，并提供了许多有用的方法来操作日期和时间。

该类包含了year、month、day、hour、minute、second等属性，并提供了一系列的方法来格式化输出日期和时间、计算日期和时间的差值、进行日期和时间的比较等。

此外，datetime模块还提供了date、time、timedelta和tzinfo等类来处理日期、时间、时间差和时区等相关操作。

其中，date类表示日期，time类表示时间，timedelta类表示时间差，tzinfo类表示时区信息。

datetime模块还提供了许多辅助函数和常量来处理日期和时间，如datetime.now()函数返回当前时间，

datetime.combine()函数可以将日期和时间合并为一个datetime对象，datetime.timedelta()函数可以计算两个日期或时间之间的差值等等。

总之，datetime模块是Python中处理日期和时间的一个非常强大的标准库，可以方便地进行各种日期和时间的操作。
"""

import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
print("当前时间：", now)

# 获取当前日期
today = datetime.date.today()
print("当前日期：", today)

# 创建一个特定日期和时间的datetime对象
dt = datetime.datetime(2022, 1, 1, 0, 0, 0)
print("特定日期和时间：", dt)

# 计算两个日期之间的差值
d1 = datetime.date(2023, 4, 12)
d2 = datetime.date(2022, 1, 1)
delta = d1 - d2
print("日期差值：", delta.days)

# 格式化输出日期和时间
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的时间：", formatted_date)

# 将字符串转换为datetime对象
str_date = "2022-01-01 00:00:00"
dt = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
print("字符串转换后的datetime对象：", dt)

# 获取本地时间和UTC时间
local_dt = datetime.datetime.now()
utc_dt = datetime.datetime.utcnow()
print("本地时间：", local_dt)
print("UTC时间：", utc_dt)

# 创建一个timedelta对象
delta = datetime.timedelta(days=7, hours=12, minutes=30, seconds=0)
print("时间差值：", delta)

# 使用timedelta对象进行时间计算
dt1 = datetime.datetime(2022, 1, 1, 0, 0, 0)
dt2 = dt1 + delta
print("时间计算结果：", dt2)
















