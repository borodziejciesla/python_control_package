import source.LTIObject as LTIObject
import numpy as np

class TransferFunction(LTIObject.LTIObject):
    
    def __init__(self, numerator, denumerator):
        self._numerator = numerator
        self._denumerator = denumerator

    # operator== overload
    def __eq__(self, other):
        self_num = self._numerator
        other_num = other.getNumerator()

        self_den = self._denumerator
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
        return 'Numerator:\n' + str(self._numerator) + '\n' + 'Denumerator:\n' + str(self._denumerator)

    # get numerator
    def getNumerator(self):
        return self._numerator

    # get denumerator
    def getDenumerator(self):
        return self._denumerator

    # inverse Transfer Function
    def __inverse(self):
        tmp = self._numerator

        self._numerator = self._denumerator
        self._denumerator = tmp

        return self

    # find serial connection of two transfer functions
    def serialConnection(self, consecutive_object):
        new_numerator = np.polymul(self._numerator, consecutive_object._numerator)
        new_denumerator = np.polymul(self._denumerator, consecutive_object._denumerator)

        return TransferFunction(new_numerator, new_denumerator)

    def parallelConnection(self, consecutive_object):
        new_numerator = np.polyadd(np.polymul(self._numerator, consecutive_object._denumerator), np.polymul(self._denumerator, consecutive_object._numerator))
        new_denumerator = np.polymul(self._denumerator, consecutive_object._denumerator)

        return TransferFunction(new_numerator, new_denumerator)

    def feedbackConnection(self, upper_line, feedback_line):
        Un = upper_line._numerator
        Ud = upper_line._denumerator
        Fn = feedback_line._numerator
        Fd = feedback_line._denumerator

        new_numerator = np.polymul(Un, Fd)
        new_denumerator = np.polyadd(np.polymul(Fd, Ud), np.polymul(Fn, Un))

        return TransferFunction(new_numerator, new_denumerator)
