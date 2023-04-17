# 在Python中，私有属性和方法可以通过在属性或方法名称前面添加两个下划线“__”来定义。

class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex  # 私有属性：在属性名称前加__

    def get_sex(self, special):
        if special == "TOM":
            return self.__sex


people1 = Person('lili', 18, 'female')

print(people1.name)  # lili

print(people1.age)   # 18

# print(people1.sex)   # 'Person' object has no attribute 'sex'
                       # 在类的外部不能直接访问对象的私有属性，需要在内部设置接口

# 要访问私有属性，可以通过类内部定义公有方法来实现。
# 公有方法可以访问私有属性并返回其值，然后在类外部调用该公有方法以获取私有属性的值。

print(people1.get_sex('TOM'))  # female

# 在上述代码中，私有属性 "__age" 只能在类内部访问。
# 但是，公有方法 "get_age()" 可以在类外部被调用，并返回私有属性的值。
# 可以在内部设置一个访问条件，外部符合条件，才允许调用这个外部方法
# 通过调用公有方法 "get_age()"，我们可以获取 Person 实例的私有属性 "__age" 的值









