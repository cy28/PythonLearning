
"""
1. 面向对象和面向过程的区别

a. 面向过程
面向过程编程和面向对象编程都是编程范式，它们描述了编程中的不同方法。
面向过程编程是一种编程方法，它以过程和函数为基础，将程序分解为一系列的步骤，每个步骤都是一个函数或过程。
它将程序视为一系列的命令，每个命令按照顺序执行，以达到所需的结果。
面向过程编程通常用于较小的程序或单个任务，它关注的是如何完成特定的任务。

b. 面向对象
面向对象编程是另一种编程方法，它将程序看作是对象的集合，
每个对象都包含了数据和方法。对象可以互相通信，并通过彼此的方法来完成任务。
面向对象编程关注的是数据和它们的交互，而不是像面向过程编程一样只关注过程。
面向对象编程通常用于大型应用程序，它允许程序员更轻松地维护和扩展程序。

c. 总结
总的来说，面向过程编程更注重程序的流程和处理方式，而面向对象编程更注重数据和数据的交互方式。
两种编程方法各有优缺点，具体使用哪种编程方法取决于具体的需求和程序的规模。


2. 类和对象的概念

类描述了一组具有相同属性和行为的对象的特征，而对象则是类的一个实例，是一个具体的实体，拥有类中定义的属性和行为。

例如，一个人可以看作是一个类，它具有一些属性，如姓名、年龄和性别等，同时还具有一些行为，如说话、走路和睡觉等。
具体的人可以看作是这个类的一个对象，每个人有自己独特的属性和行为。

"""

# 定义类
"""
class ClassName:
    # class variables and methods

    def __init__(self, parameter1, parameter2, ...):  # 定义属性
        # constructor

    def method1(self, parameter1, parameter2, ...):   # 定义方法
        # method 1 definition

    def method2(self, parameter1, parameter2, ...):
        # method 2 definition

    # ...
"""


class Person:  # 定义一个名为Person的类
    def __init__(self, name, age):  # 定义属性的初始化方法，self表示对象本身，name和age是对象的属性
        self.name = name            # 初始化对象的name属性
        self.age = age              # 初始化对象的age属性

    def say_hello(self):            # 定义一个方法，输出问候语，self表示对象本身
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")


# 创建一个Person类的实例
person = Person("Alice", 25)

# 调用实例的方法
person.say_hello()  # 输出问候语












