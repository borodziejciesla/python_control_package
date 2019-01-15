import numpy as np
import scipy as sp
import abc

class LTIObject(object):
    __metaclass__ = abc.ABCMeta  
    _is_valid = False  
    
    @abc.abstractmethod
    def bode(self):
        pass

    @abc.abstractmethod
    def nyquist(self):
        pass

    @abc.abstractmethod
    def printSystem(self):
        pass

    def isValid(self):
        return self._is_valid

    def eigenvalues(self):
        pass

    ## Static methods
    # Serial connection
    @staticmethod
    def _isValidShapeForSerialConnection(input_object, output_object):
        if (input_object.isValid() and output_object.isValid()):
            return (input_object._output_dimension == output_object._control_dimension)
        else:
            return False

    def __mul__(self, other):
        return LTIObject.serial(self, other)

    @staticmethod
    def serial(*objects):
        objects_number = len(objects)
        try:
            new_object = objects[0]

            for idx in range(1, objects_number):
                new_object = new_object.serialConnection(objects[idx])

            return new_object
        except:
            print('No objects given!')

    # Parallel connection
    @staticmethod
    def _isValidShapeForParallelConnection(upper_object, lower_object):
        if (upper_object.isValid() and lower_object.isValid):
            return (upper_object._control_dimension == lower_object._control_dimension) \
                and (upper_object._output_dimension == lower_object._output_dimension)
        else:
            return False

    def __add__(self, other):
        return LTIObject.parallel(self, other)

    @staticmethod
    def parallel(*objects):
        objects_number = len(objects)
        try:
            new_object = objects[0]

            for idx in range(1, objects_number):
                new_object = new_object.parallelConnection(objects[idx])
            
            return new_object
        except:
            print('No objects given!')

    # Feedback connection
    @staticmethod
    def _isValidShapeForFeedbackConnection(direct_line, feedback_line):
        if (direct_line.isValid() and feedback_line.isValid()):
            return (direct_line._output_dimension == feedback_line._control_dimension) \
                and (direct_line._control_dimension == feedback_line._output_dimension)
        else:
            return False

    @staticmethod
    def feedback(upper_line, feedback_line):
        new_object = upper_line
        return new_object.feedbackConnection(upper_line, feedback_line)
