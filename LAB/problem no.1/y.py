from a import A
from b import B

class Y(A, B):
    def __init__(self):
        self.__Y = True
        A.__init__(self)
        B.__init__(self)
    def getSelfY(self):
        return f"Y is {self.__Y}"