import numpy as np
import abc

class LTIObject(object):
    __metaclass__ = abc.ABCMeta    
    
    @abc.abstractmethod
    def bode(self):
        pass

    @abc.abstractmethod
    def nyquist(self):
        pass
