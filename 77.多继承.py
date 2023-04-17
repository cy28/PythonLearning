# 多继承是指一个子类可以继承多个父类的属性和方法。
# 下面是一个Python的示例代码，演示了如何通过多继承实现一个具有多个父类特征的子类：
# 定义父类1
class Parent1:
    def __init__(self):
        self.name = "Parent1"

    def greet(self):
        print(f"Greetings from {self.name}!")

    def method1(self):
        print(f"This is method1 from {self.name}.")


# 定义父类2
class Parent2:
    def __init__(self):
        self.name = "Parent2"

    def greet(self):
        print(f"Greetings from {self.name}!")

    def method2(self):
        print(f"This is method2 from {self.name}.")


# 定义父类3
class Parent3:
    def __init__(self):
        self.name = "Parent3"

    def greet(self):
        print(f"Greetings from {self.name}!")

    def method3(self):
        print(f"This is method3 from {self.name}.")


# 定义子类，继承自Parent1, Parent2和Parent3
class Child(Parent1, Parent2, Parent3):
    def __init__(self):          # 初始化属性
        Parent1.__init__(self)   # 继承属性
        Parent2.__init__(self)
        Parent3.__init__(self)
        self.age = 10

    def greet(self):
        print(f"Greetings from {self.name}! I'm {self.age} years old.")

    def method4(self):
        print(f"This is method4 from Child.")


"""

在上面的代码中，我们定义了三个父类，每个父类都有自己的属性和方法。
然后我们定义了一个子类Child，继承了三个父类的所有属性和方法，并添加了自己的属性和方法。
在子类Child的构造函数中，我们分别调用了父类的构造函数，以初始化从父类继承来的属性。
我们可以创建一个Child类的实例，并调用它继承的所有属性和方法，以及它自己定义的属性和方法。例如

"""

# 创建Child类实例
c = Child()

# 调用从父类继承来的方法和属性
c.greet()   # Output: Greetings from Parent1! I'm 10 years old.
c.method1() # Output: This is method1 from Parent1.  # 调用父类的方法
c.method2() # Output: This is method2 from Parent2.
c.method3() # Output: This is method3 from Parent3.

# 调用子类自己的方法和属性
c.method4() # Output: This is method4 from Child.


# 在这个例子中，我们可以看到，子类继承了所有的父类属性和方法，并添加了自己的属性和方法。
# 同时，子类还覆盖了从多个父类继承来的方法，这表明在多继承中，如果多个父类有同名方法，子类将继承第一个出现的父类的方法。









