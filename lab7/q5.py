import math
from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
shape1 = Rectangle(10, 20)
shape2 = Circle(5)
print(shape1.area())
print(shape1.perimeter())
print(shape2.area())
print(shape2.perimeter())