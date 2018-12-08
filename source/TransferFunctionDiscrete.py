import TransferFunction

class TransferFunctionDiscrete(TransferFunction.TransferFunction):

    def __init__(self, numerator, denumerator):
        TransferFunction.TransferFunction.__init__(self, numerator, denumerator)

    def bode(self):
        pass