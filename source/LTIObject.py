import numpy as np
import scipy as sp
import abc

class LTIObject(object):
    __metaclass__ = abc.ABCMeta    
    
    @abc.abstractmethod
    def bode(self):
        pass

    @abc.abstractmethod
    def nyquist(self):
        pass

    @abc.abstractmethod
    def printSystem(self):
        pass

    # Static methods
    @staticmethod
    def serial():
        pass

    @staticmethod
    def parallel():
        pass

    @staticmethod
    def feedback():
        pass
