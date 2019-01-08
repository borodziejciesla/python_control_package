import source.LTIObject as LTIObject
import numpy as np

class TransferFunction(LTIObject.LTIObject):
    
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    # operator== overload
    def __eq__(self, other):
        self_num = self.numerator
        other_num = other.getNumerator()

        self_den = self.denumerator
        other_den = other.getDenumerator()

        if (len(self_num) == len(other_num)):
            for i in range(0, len(other_num)):
                if (self_num[i] != other_num[i]):
                    return False
        else:
            return False

        if (len(self_den) == len(other_den)):
            for i in range(0, len(other_den)):
                if (self_den[i] != other_den[i]):
                    return False
        else:
            return False

        return True

    # convert to string
    def __str__(self):
        return 'Numerator:\n' + str(self.numerator) + '\n' + 'Denumerator:\n' + str(self.denumerator)

    # get numerator
    def getNumerator(self):
        return self.numerator

    # get denumerator
    def getDenumerator(self):
        return self.denumerator

    # find serial connection of two transfer functions
    def serialConnection(self, consecutive_object):
        new_numerator = np.polymul(self.numerator, consecutive_object.numerator)
        new_denumerator = np.polymul(self.denumerator, consecutive_object.denumerator)

        result = TransferFunction(new_numerator, new_denumerator)

        return result

    def parallelConnection(self, consecutive_object):
        new_numerator = np.polyadd(np.polymul(self.numerator, consecutive_object.denumerator), np.polymul(self.denumerator, consecutive_object.numerator))
        new_denumerator = np.polymul(self.denumerator, consecutive_object.denumerator)

        result = TransferFunction(new_numerator, new_denumerator)

        return result


obj_1 = TransferFunction([1], [1, 2])
obj_2 = TransferFunction([1], [1, 2])
obj = obj_1 * obj_2
obj_ref = TransferFunction([1], [1, 4, 4])