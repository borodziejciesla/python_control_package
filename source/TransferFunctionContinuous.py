import source.TransferFunction as TransferFunction

class TransferFunctionContinuous(TransferFunction.TransferFunction):

    def __init__(self, numerator, denumerator):
        TransferFunction.TransferFunction.__init__(self, numerator, denumerator)

    def bode(self):
        pass