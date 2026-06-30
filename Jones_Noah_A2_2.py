from abc import ABC, abstractmethod
import math
class Shape:
    
    def __eq__(self, other):
        if self.area() == other.area():
            print("The areas are equal")
        else:
            print("The areas are not equal")
        
    def __gt__(self, other):
        if self.area() > other.area():
            print(self.name+" is greater than "+other.name)
        else:
            print(self.name+" is not greater than "+other.name)
        
    def __lt__(self, other):
        if self.area() < other.area():
            print(self.name+" is less than "+other.name)
        else:
            print(self.name+" is less than "+other.name)
    
    @abstractmethod
    def perimeter():
        pass
    
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self,name,radius):
        self.name=name
        self.rad=radius
    
    def perimeter(self):
        return (self.rad*2*3.14)
   
    
    def area(self):
        return (self.rad*self.rad*3.14)
    
    def __eq__(self, other):
        super().__eq__(other)
    
    def __gt__(self, other):
        super().__gt__(other)
    
    def __lt__(self, other):
        super().__lt__(other)

class Rectangle(Shape):
    def __init__(self, name,l,w):
        self.name=name
        self.length=l
        self.width=w
    
    def perimeter(self):
        return (2*self.length+2*self.width)
    
    def area(self):
        return (self.length*self.length)
    
    def __eq__(self, other):
        super().__eq__(other)
    
    def __gt__(self, other):
        super().__gt__(other)
    
    def __lt__(self, other):
        super().__lt__(other)

class Square(Shape):
    def __init__(self, name,s):
        self.name=name
        self.sides=s
    
    def perimeter(self):
        return(self.sides*4)
    
    def area(self):
        return(self.sides*self.sides)
    
    def __eq__(self, other):
        super().__eq__(other)
    
    def __gt__(self, other):
        super().__gt__(other)
    
    def __lt__(self, other):
        super().__lt__(other)

class Triangle(Shape):
    def __init__(self,name,sides):
        self.name=name
        self.sides=sides
    
    def perimeter(self):
        return(3*self.sides)
    
    def area(self):
        return((math.sqrt(3/4))*(self.sides*self.sides))
    
    def __eq__(self, other):
        super().__eq__(other)
    
    def __gt__(self, other):
        super().__gt__(other)
    
    def __lt__(self, other):
        super().__lt__(other)

o1=Circle("circle",2)
o2=Rectangle("rectanglr",2,3)
o3=Square("square",4)
o4=Triangle("triangle",6)
print(o1.perimeter())
print(o1.area())
print(o2.perimeter())
print(o2.area())
print(o3.perimeter())
print(o3.area())
print(o4.perimeter())
print(o4.area())
o1==o2
o3==o4
o1>o2
o3<o4