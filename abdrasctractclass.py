# https://metanit.com/python/tutorial/7.8.php

import abc, math


class Shape(abc.ABC):
    """
    aбстрактный класс геометрической фигуры
    :param x: - абсцисса центра
    :param y: - ордината центра
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y 
         
    @abc.abstractmethod     
    def area (self): pass           # абстрактны метод
     
    def print_point(self):
        '''
        неабстрактный метод возвращает
        координаты центра фигуры
        '''        
        print(f"X: {self.x}, \tY: {self.y}")
 
 
class Rectangle(Shape):
    '''
    класс прямоугольника
    '''
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def area (self): return self.width * self.height

 
class Circle(Shape):
    '''
    класс круга
    '''
    def __init__(self, xCenter, yCenter, radius):
        super().__init__(xCenter, yCenter)
        self.radius = radius
    
    def area (self): return self.radius * self.radius * math.pi
    
 
def print_area(figure):
    print(f"Area: {figure.area():.2f}")


if __name__ == '__main__':

    rect = Rectangle(10, 20, 100, 100)
    rect.print_point()      # X: 10   Y: 20

    circle = Circle(0, 0, 30)
    circle.print_point()    # X: 0,   Y: 0

    print_area(rect)        # Area: 10000.00
    print_area(circle)      # Area: 2827.43