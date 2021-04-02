class Point:
    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
        self.s = x*y

pt = Point(2,2)
pt2 = Point(5,5)
pt.s = 10
print(pt.s,pt2.s)