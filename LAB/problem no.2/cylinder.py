

class Cylinder():
    def __init__(self, height = 1.0):
        self.__height = height

    def getHeight(self):
        return self.__height
    
    def setHeight(self,height):
        self.__height = height
    
    def toString(self):
        return f"Cylinder(Circle({self.getRadius()},{self.getColor()}), {self.getHeight()})"
        
    def getVolume(self):
        return self.getArea() * self.getHeight()
