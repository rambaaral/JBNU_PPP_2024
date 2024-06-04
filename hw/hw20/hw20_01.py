#class를 이용해 도형 클래스 완성하기
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h*self.v
    def perimeter(self):
        return 2*self.h+2*self.v
    
class Triangle(Shape):
    def __init__(self,h,v):
        self.h = h
        self.v = v
    def area(self):
        return self.h*self.v/2
    def perimeter(self):
        return 3*self.v
    
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return round(math.pi*self.r**2,2)
    def perimeter(self):
        return round(2*math.pi*self.r,2)
    
class RegularHexagon(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return round(6*3**(1/2)/4*self.r**2,2)
    def perimeter(self):
        return 6*self.r
    
def main():
    shapelist = []
    shapelist.append(Rectangle(5,6))
    shapelist.append(Triangle(5,7))
    shapelist.append(Circle(5))
    shapelist.append(RegularHexagon(6))

    for shape in shapelist:
        print(shape)
        print(f"넓이{shape.area()}")
        print(f"둘레{shape.perimeter()}")

if __name__ == "__main__":
    main()