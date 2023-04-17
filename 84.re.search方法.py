import re

# 定义输入字符串和要搜索的模式
input_str = "快速的棕色狐狸跳过了懒狗。"
pattern = "狐狸"

# 使用 re.search() 函数在输入字符串中查找第一个匹配项
match = re.search(pattern, input_str)

# 检查是否找到了匹配项
if match:
    print("找到匹配项！")
    # 打印匹配项的开始和结束索引
    print("匹配项的开始索引为", match.start(), "，结束索引为", match.end())
    # 打印实际匹配的字符串
    print("匹配的字符串为:", match.group())
else:
    print("没有找到匹配项。")













































