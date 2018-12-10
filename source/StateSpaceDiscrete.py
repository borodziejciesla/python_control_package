import source.StateSpace as StateSpace

class StateSpaceDiscrete(StateSpace.StateSpace):

    def __init__(self, A, B, C, D):
        StateSpace.StateSpace.__init__(self, A, B, C, D)

    def bode(self):
        pass