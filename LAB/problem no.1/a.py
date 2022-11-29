from m import M

class A(M):
    def __init__(self):
        self.__A = True
        M.__init__(self)
    
    def getSelfA(self):
        return f"A is {self.__A}"
