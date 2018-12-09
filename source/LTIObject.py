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
    def serial(*objects):
        objects_number = len(objects)
        try:
            new_object = objects[0]

            for idx in range(1, objects_number):
                new_object.serialConnection(objects[idx])

            return new_object
        except:
            print('No objects given!')

    @staticmethod
    def parallel(*objects):
        objects_number = len(objects)
        try:
            new_object = objects[0]

            for idx in range(1, objects_number):
                new_object.parallelConnection(objects[idx])
            
            return new_object
        except:
            print('No objects given!')

    @staticmethod
    def feedback(*objects):
        pass
