class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.x = x
        self.y = y

    @staticmethod  # можно работать только с методами и свойствами данного класса не указывая self
    def getCount():
        return Point.__count


pt = Point()
pt2 = Point()
pt3 = Point()
print(pt2.getCount(), Point.getCount())  # если не обявлять getCount статическим методом то вызов через класс невозможно


class Singl_ton:
    __instance = None

    # этот метот не будет работать в дочерних экземплярах класса
    def __new__(cls, *args, **kwargs):  # выполняется перед тем как создать экземпляр класса,
        # в нем он и создается, перегружая его мы контролируем их количество
        # проверяем что __instance не равняется классу cls по умаолчанию так и есть
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Singl_ton, cls).__new__(cls)  # создаем экземпляр класса
        else:
            print(f"Экземпляр класса {Singl_ton} уже создан")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt4 = Singl_ton(5,5)
pt5 = Singl_ton()
pt6 = Singl_ton()

print(id(pt4), id(pt5), id(pt6), sep="\n")

