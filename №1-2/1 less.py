class Point:
    x = 1
    y = 5

    def setCoords(self, x, y):
        print(self.__dict__)  # вывод всех локальных переменных pt
        self.x = x
        self.y = y


pt = Point()
print(pt.x, pt.y)
# создадим локальные переменные
pt.x = 10
pt.y = 10
print(pt.x, pt.y)

print(getattr(pt, "x"))
print(getattr(pt, "a", False))
print(hasattr(pt, "a"))
print(isinstance(pt, Point))  # проверка наследования
print("#1")




class Point1:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def setCoords(self, x, y):
        print(self.__dict__)  # вывод всех локальных переменных pt
        self.x = x
        self.y = y


pt1 = Point1(8,8)
pt3 = Point1()
pt1.setCoords(20, 30)
print(pt1.__dict__, pt3.__dict__ )
pt2 = Point1(7,7)
print(pt2.__dict__)


class test:
    def __init__(self):
        print(self)



