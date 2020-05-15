# About classes and constructor!
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point(10, 20)
point1.x = 2
print(point1.x)
point1.move()
point1.draw()

point2 = Point(10, 20)
print(point2.x)
point2.draw()
