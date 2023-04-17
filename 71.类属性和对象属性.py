# 在Python中，类属性是指在类定义中直接定义的属性，它们属于整个类，而不是某个特定的对象。
# 对象属性是指在实例化类时为特定对象定义的属性，它们属于该特定对象。


class MyClass:
    class_attr = "I am a class attribute"

    def __init__(self, obj_attr):
        self.obj_attr = obj_attr


# 创建两个对象
obj1 = MyClass("I am the attribute of obj1")
obj2 = MyClass("I am the attribute of obj2")

# 访问类属性
print(MyClass.class_attr)  # 输出: "I am a class attribute"
print(obj1.class_attr)     # 输出: "I am a class attribute"
print(obj2.class_attr)     # 输出: "I am a class attribute"

# 访问对象属性
print(obj1.obj_attr)  # 输出: "I am the attribute of obj1"
print(obj2.obj_attr)  # 输出: "I am the attribute of obj2"

# 修改类属性和对象属性
MyClass.class_attr = "I am a new class attribute"
obj1.obj_attr = "I am a new attribute of obj1"

# 再次访问属性
print(MyClass.class_attr)  # 输出: "I am a new class attribute"
print(obj1.class_attr)     # 输出: "I am a new class attribute"
print(obj2.class_attr)     # 输出: "I am a new class attribute"
print(obj1.obj_attr)       # 输出: "I am a new attribute of obj1"
print(obj2.obj_attr)       # 输出: "I am the attribute of obj2"


"""
在上述示例中，class_attr 是一个类属性，obj_attr 是对象属性。
当我们创建对象时，每个对象都有其自己的 obj_attr 值，但是它们共享相同的 class_attr 值。
我们还可以看到，当我们修改类属性时，它会影响所有对象，但当我们修改对象属性时，只会影响该特定对象的属性。

"""











