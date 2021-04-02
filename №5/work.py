"""
объявите клаcс прямоугольник, в котором имеется статический метод, вычисляющий площадь его. Этот метод принимает два парамета(ширину и длину), вызывается в коснтрукторе
для вычисления площади конкретного прямоугольника и результат присваивается локальному свойству создаваемого экземпляра класса
"""


class Rectangle_dis:
    __area = 0

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Rectangle:
    __area = Rectangle_dis()

    def __init__(self, width: int = 0, length: int = 0):
        self.width = width
        self.length = length
        self.__area = width * length


a = Rectangle(5, 5)
b = Rectangle(4, 4)
print(a.__dict__, b)


class Rectangle1:
    def __init__(self, width: int = 0, length: int = 0):
        self.width = width
        self.length = length
        self.__area = Rectangle1.__area(self.width, self.length)

    @staticmethod
    def __area(width: int, length: int):
        return width * length

    def setArea(self):
        return self.__area


a = Rectangle1(3, 3)
b = Rectangle1(2, 2)
a.width = 2000
print(a.setArea(), b.setArea())
"""
создайте класс Dog, в каждом его экземпляре создавайте несколько локальных свойств( напрмер: Имя, возраст, порода)
и сдалейте так, чтобы можно было создавать не более пяти экземпляров этого класса
"""


class Dog:
    __count = 0

    def __new__(cls, *args, **kwargs):
        if Dog.__count < 5:
            Dog.__count += 1
            return super(Dog, cls).__new__(cls)
        else:
            print(f"Экземпляр класса {Dog} уже создан")

    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed


first = Dog("Bim", 10, "pudel")
print(first.name)
second = Dog("Charli", 5, "spaniel")
third = Dog("Reks", 2, "dog")
fourth = Dog("K9", 7, "pop")
fifth = Dog("Yellow", 9, "Popug")
sixth = Dog("1", 1, "1")
