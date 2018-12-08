import LTIObject

class StateSpace(LTIObject.LTIObject):
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def printSystem(self):
        print(self.A)