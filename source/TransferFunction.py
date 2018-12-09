import source.LTIObject as LTIObject
import numpy as np

class TransferFunction(LTIObject.LTIObject):
    
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def printSystem(self):
        print('Numerator:')
        print(self.numerator)
        print('Denumerator:')
        print(self.denumerator)

    def getNumerator(self):
        return self.numerator

    def getDenumerator(self):
        return self.denumerator

    def serialConnection(self, consecutive_object):
        new_numerator = np.polyadd(np.polymul(self.numerator, consecutive_object.denumerator), np.polymul(self.denumerator, consecutive_object.numerator))
        new_denumerator = np.polymul(self.denumerator, consecutive_object.denumerator)

        return TransferFunction(new_numerator, new_denumerator)
