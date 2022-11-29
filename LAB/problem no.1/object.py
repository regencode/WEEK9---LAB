from x import X
from y import Y
from z import Z

class Object(X,Y,Z):
    def __init__(self):
        self.__object = True
        X.__init__(self)
        Y.__init__(self)
        Z.__init__(self)

n = Object()


print(n.getSelfM())
print(n.getSelfA())
print(n.getSelfB())
print(n.getSelfX())
print(n.getSelfY())
print(n.getSelfZ())
