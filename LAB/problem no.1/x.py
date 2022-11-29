from a import A

class X(A):
    def __init__(self):
        self.__X = True
        A.__init__(self)
    def getSelfX(self):
        return f"X is {self.__X}"
    
n = X()
