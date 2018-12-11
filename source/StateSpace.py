import source.LTIObject as LTIObject

class StateSpace(LTIObject.LTIObject):
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    # operator== overloaded
    def __eq__(self, other):
        return ((self.A == other.A) and (self.B == other.B) and (self.C == other.C) and (self.D == other.D))

    # convert to string
    def __str__(self):
        return 'State Matrix A:\n' + str(self.A) + '\nControl Matrix B:\n' + str(self.B) + '\nOutput Matrix C:\n' + str(self.C) + '\nDirect Control Matrix D:\n' + str(self.D)

    def getA(self):
        return self.A

    def getB(self):
        return self.B

    def getC(self):
        return self.C

    def getD(self):
        return self.D