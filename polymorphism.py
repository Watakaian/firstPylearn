class Shape:
    def draw(self):
        print('Drawing shape')


class Square:
    def draw(self):
        print('Drawing square')


class Rectangle:
    def draw(self):
        print('Drawing rectangle')


shape = Shape()
rectangle = Rectangle()
square = Square()
shape.draw()
rectangle.draw()
square.draw()
