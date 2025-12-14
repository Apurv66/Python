from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5

class Circle(Shape):
    def area(self):
        return 3.14 * 4 * 4

r = Rectangle()
c = Circle()

print(r.area())
print(c.area())
