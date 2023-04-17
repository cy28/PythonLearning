"""
练习，根据学生的分数，将学生的成绩做不同等级的划分
大于90分表示优秀
80-90分表示良+
70-80分表示良
60-70分表示一般
低于60分表示不及格
"""

score = int(input("请输入你的成绩："))

if score > 90:
    print("优秀")
elif score > 80:
    print("良+")
elif score > 70:
    print("良")
elif score > 60:
    print("一般")
else:
    print("不及格")




























