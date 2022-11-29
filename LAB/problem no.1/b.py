from m import M

class B(M):
    def __init__(self):
        self.__B = True
        M.__init__(self)

    def getSelfB(self):
        return f"B is {self.__B}"
