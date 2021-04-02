

# обычный класс
class Point:
    z= 10
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt = Point(5, 10)
print(pt.x, pt.y)
# переопределение атрибута класса
pt.x = 100
pt.y = "aba"
print(pt.x, pt.y)


# класс с статическими параметрамми
class Point1:
    WIDTH = 10


    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x): # приватный метод на проверку является ли объект числом
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False


    def setCord(self, x, y):  # публичный метод (сеттор)обновление статических атрибутов объекта класса
        # проверяем чсло ли x y
        if Point1.__checkValue(x) and Point1.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCord(self):  # публичный метод (геттер) вызов атрибутов объекта класса
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == "_Point.__x":
            return "Частная переменная"
        else:
            return object.__getattribute__(self, item)

    # метод не позволяющий менять атрибут
    def __setattr__(self, key, value):
        if key == "WIDTH":
            raise AttributeError
        else:
            self.__dict__[key] = value

    # метод если обратиться к несуществуещиму свойству класса
    def __getattr__(self, item):
        print("__getattr__:" + item)





pt1 = Point1(7, 7)
print(pt1.getCord())
pt1.setCord(10, 10)
print(pt1.getCord())
#pt1.WIDTH = 5

class Point2:
    __slots__ = ["__x", "__y", "z"] # разрешенные свойства экземпляров класса
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

pt3 = Point2(9, 9)
# pt3.f = 1  будет ошибка потому что в __slots__ непрописанно f
