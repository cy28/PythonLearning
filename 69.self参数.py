# 在Python中，self是一个特殊的参数，它是用来引用对象本身的。
# self在类的方法中使用，指的是该方法所属的实例对象。
# 以下是一个示例：
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name, "and I'm", self.age, "years old.")


person = Person("John", 30)
person.say_hello()

# 在上面的示例中，self参数在__init__方法和say_hello方法中都被使用了。
# 在__init__方法中，self用于引用新创建的实例对象，以便可以在对象中保存实例变量。
# 在say_hello方法中，self用于引用调用该方法的实例对象，以便可以访问该实例对象中保存的变量。
# 在Python中，self不是关键字，你可以使用任何名称来代替self，但是，约定俗成的做法是使用self作为该参数的名称。













