class MyClass:
    type = 'human'  # 定义一个类属性

    def __init__(self, name, age):  # 初始化实例属性
        self.name = name            # 定义实例属性
        self.age = age              # self是一个特殊参数，用来表示将来要创建的对象

    def instance_method(self, food):            # 定义一个实例方法
        print("This is an instance method")
        print(self.name+'正在吃'+food)           # 实例方法可以访问实例属性

    @classmethod                                # 定义一个类方法
    def class_method(cls):                      # 参数cls指的是类对象
        print("This is a class method")
        print(cls.type)

    @staticmethod
    def static_method():
        print("This is a static method")


"""
解释：
1. 这里定义了一个名为MyClass的类，其中包含了一个实例方法、一个类方法和一个静态方法。

2. instance_method是一个实例方法，因为它的第一个参数是self，这个参数是在调用方法时自动传递的实例对象本身。

3. class_method是一个类方法，因为它使用@classmethod装饰器来定义。在方法内部，第一个参数是cls，它代表了类本身，而不是实例对象。
因此，在方法内部，可以访问类属性x。

4.static_method是一个静态方法，因为它使用@staticmethod装饰器来定义。
它没有任何默认参数，因此不能访问实例属性或类属性。这个方法在类和实例之间没有任何区别。
"""

# 如何调用这些方法：

# 创建类实例(对象)
obj = MyClass('chen', 23)

# 调用实例方法 需要访问到实例中的属性
obj.instance_method('红烧肉')     # This is an instance method
                                 # chen正在吃红烧肉

# 调用类方法  需要访问到类中的属性
MyClass.class_method()           # This is a class method
                                 # human

# 调用静态方法  类属性和对象属性都没有用到 可以通过类名直接调用
MyClass.static_method()          # This is a static method


"""
输出结果如下：

This is an instance method
x = 0 y = 100

This is a class method
x = 0

This is a static method

"""