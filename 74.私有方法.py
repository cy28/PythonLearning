class MyClass:
    def public_method(self):
        print("Calling public_method")
        self.__private_method()

    def __private_method(self):
        print("Calling private_method")


my_object = MyClass()
my_object.public_method()


"""
1. 定义了一个名为 MyClass 的类，其中包含一个公共方法 public_method 和一个私有方法 __private_method。
2. 类中的公共方法可以调用私有方法。
3. 在类的外部，我们创建了一个 MyClass 的实例 my_object，然后调用了它的公共方法 public_method。
4. 当调用公共方法时，会先输出一行文本 "Calling public_method"，然后调用私有方法 __private_method。
5. 在私有方法中，也输出了一行文本 "Calling private_method"。

注意：
的是，私有方法的名称前面有两个下划线 __，这意味着它是一个私有方法，只能在类的内部使用。
在类的外部，我们无法直接访问或调用私有方法。
但是，在类的内部，我们可以通过 self.__private_method() 的方式来调用私有方法。
"""