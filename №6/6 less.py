# наследование классов, режима доступа protected

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # переопределим метот str для возвращения координат
    def __str__(self):
        return f"({self.__x},{self.__y})"


print(issubclass(Point, object))  # проверка дочерности


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width  # частное свойство

    def getWidth(self):  # метод получения частного свойства
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print("Переопределяем")
        super().__init__(*args)  # переберает в правильно порядке выше стоящие классы

    def drawLine(self):
        print(f"рисуем линию: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


class Rect(Prop):
    def drawLine(self):
        print(f"рисуем прямоугольник: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


l = Line(Point(1, 2), Point(10, 20))
l = Rect(Point(15, 25), Point(25, 40))

l.drawLine()
