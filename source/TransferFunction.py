import source.LTIObject as LTIObject
import numpy as np

class TransferFunction(LTIObject.LTIObject):
    
    def __init__(self, numerator, denumerator, create_empty = False, input_name = None, output_name = None):
        if (create_empty == False):
            self.__verifyVectorShape(numerator, denumerator)

            if self._is_valid:
                self._numerator = numerator
                self._denumerator = denumerator

                self._state_dimension = denumerator.__len__()
                self._control_dimension = 1
                self._output_dimension = 1
            else:
                self._numerator = []
                self._denumerator = []

                self._state_dimension = []
                self._control_dimension = []
                self._output_dimension = []
        else:
            self._is_valid = False

            self._numerator = []
            self._denumerator = []

            self._state_dimension = []
            self._control_dimension = []
            self._output_dimension = []

        try:
            super().__init__(input_name, output_name)
        except Exception as error:
            print(error)
        except:
            print("Unknown error")

    def __verifyVectorShape(self, numerator, denumerator):
        if (numerator.__len__() < denumerator.__len__()):
            self._is_valid = True
        else:
            self._is_valid = False

    # Operator == overload
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

    # Get numerator
    def getNumerator(self):
        return self._numerator

    # Get denumerator
    def getDenumerator(self):
        return self._denumerator

    # Inverse Transfer Function
    def __inverse(self):
        tmp = self._numerator

        self._numerator = self._denumerator
        self._denumerator = tmp

        return self

    ## Analysis
    def eigenvalues(self):
        if self.isValid():
            return np.roots(self._numerator)
        else:
            return []

    ## Connections
    def serialConnection(self, consecutive_object):
        if TransferFunction._isValidShapeForSerialConnection(self, consecutive_object):
            new_numerator = np.polymul(self._numerator, consecutive_object._numerator)
            new_denumerator = np.polymul(self._denumerator, consecutive_object._denumerator)

            return TransferFunction(new_numerator, new_denumerator)
        else:
            return TransferFunction([], [], True)

    def parallelConnection(self, consecutive_object):
        if TransferFunction._isValidShapeForParallelConnection(self, consecutive_object):
            new_numerator = np.polyadd(np.polymul(self._numerator, consecutive_object._denumerator), np.polymul(self._denumerator, consecutive_object._numerator))
            new_denumerator = np.polymul(self._denumerator, consecutive_object._denumerator)

            return TransferFunction(new_numerator, new_denumerator)
        else:
            return TransferFunction([], [], False)

    def feedbackConnection(self, upper_line, feedback_line):
        if TransferFunction._isValidShapeForFeedbackConnection(upper_line, feedback_line):
            Un = upper_line._numerator
            Ud = upper_line._denumerator
            Fn = feedback_line._numerator
            Fd = feedback_line._denumerator

            new_numerator = np.polymul(Un, Fd)
            new_denumerator = np.polyadd(np.polymul(Fd, Ud), np.polymul(Fn, Un))

            return TransferFunction(new_numerator, new_denumerator)
        else:
            return TransferFunction([], [], False)
