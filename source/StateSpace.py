import source.LTIObject as LTIObject

class StateSpace(LTIObject.LTIObject):
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def printSystem(self):
        print('State Matrix A:')
        print(self.A)
        print('Control Matrix B:')
        print(self.B)
        print('Output Matrix C:')
        print(self.C)
        print('Direct Control Matrix D:')
        print(self.D)

    def getA(self):
        return self.A

    def getB(self):
        return self.B

    def getC(self):
        return self.C

    def getD(self):
        return self.D