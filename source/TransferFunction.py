import LTIObject

class TransferFunction(LTIObject.LTIObject):
    
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def printSystem(self):
        print(self.numerator)