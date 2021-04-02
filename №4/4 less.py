"""
объекты свойства (property)
"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    # геттеры и сееторы сделаем приватными
    def __getCoordx(self):
        print("Вызов __getCoordX")
        return self.__x

    def __setCordx(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("неверный формат данных")

    def __delCoordX(self):
        print("Удаление свойства")
        del self.__x

    coordX = property(__getCoordx, __setCordx, __delCoordX)


pt = Point(1, 2)
pt.coordX = 100  # записать данные
x = pt.coordX  # чтение данных
print(x)
del pt.coordX  # удаляем приватную переменную х из экзмпляра класса pt
pt.coordX = 7
y = pt.coordX
print(y)

print("______________")


# либо можно написать подругому
class Point1:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        if Point1.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("неверный формат данных")

    @coordX.deleter
    def coordX(self):
        print("Удаление свойства")
        del self.__x


pt1 = Point1(1, 2)
pt2 = Point1(3, 3)
print(pt1.coordX)
print(pt2.coordX)
pt1.coordX = 100
x = pt1.coordX
print(x)
del pt1.coordX
pt1.coordX = 7
y = pt1.coordX
print(y)

# еще один вариант через дискрипторы
print("__________")


class CoordValue:  # класс дискриптора
    def __set_name__(self, owner, name):  # с версии 3.6 можно использовать вместо __init__ и не задавать в классе имена
        self.__name = name

    """def __init__(self, name):
        self.__name = name"""

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
        # instance  экзмемпляры точек хранились непосредственно в наших экземплярах класса

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
    # def __delete__(self, instance):
    # return self.__value


class Point3:
    coordX = CoordValue()  # имеена большен не нужны,автоматически создаются  coordX
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt3 = Point3(5, 5)

print(pt3.coordX)
pt3.coordX = 9
print(pt3.coordX)
pt4 = Point3(2, 2)
print(pt4.coordX, pt4.coordY)
