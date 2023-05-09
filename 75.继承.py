"""
继承是面向对象编程中的一种重要概念，它允许一个类（称为子类或派生类）从另一个类（称为父类或基类）继承属性和方法。
在Python中，继承是通过创建一个新类并在其中指定要继承的现有类来实现的。

"""
# 下面是一个简单的代码示例，演示如何使用Python实现继承：


# 父类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


# 子类
class Dog(Animal):                          # 在子类中继承父类，只需要在参数列表中写上父类名即可
    def __init__(self, name, age, breed):   # 先初始化
        # 有两种继承父类构造函数的写法
        # 第一种，通过父类名字调用父类的构造函数
        # Animal.__init__(name, age)        # 再继承父类属性
        # 第二种，隐式继承父类的构造函数
        super().__init__(name, age)         # 再继承父类属性
        self.breed = breed                  # 初始化自己的属性

    def speak(self):
        return "Woof!"


# 子类
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"


"""
解释：

1. 定义了一个名为Animal的基类，它具有两个属性（名称和年龄）和一个空的speak()方法。

2. 定义了两个派生类Dog和Cat，它们分别继承了Animal类，并分别添加了它们自己的属性和实现了speak()方法。

3. 在Dog和Cat类的构造函数中，我们使用了super()函数调用基类的构造函数，以便在子类中初始化名称和年龄属性。这样就可以避免在子类中重复编写基类的代码。

4. 最后，我们实现了每个类自己的speak()方法，这样每个派生类就可以根据自己的需要定义自己的声音。
"""




















