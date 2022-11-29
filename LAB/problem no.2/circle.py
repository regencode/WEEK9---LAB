import math
from cylinder import Cylinder

class Circle(Cylinder):
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color
        Cylinder.__init__(self)
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color

    def toString(self):
        return f"Circle({self.__radius}, {self.__color}"
    
    def getArea(self):
        return math.pi * (self.__radius ** 2)