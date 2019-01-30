import numpy as np
import scipy as sp
import abc

class LTIObject(object):
    __metaclass__ = abc.ABCMeta  
    _is_valid = False
    _input_name = None
    _output_name = None
    _state_dimension = None
    _control_dimension = None
    _output_dimension = None

    def __init__(self, input_name, output_name):
        self.setInputNames(input_name)
        self.setOutputNames(output_name)
    
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

    ## Names
    # getes
    def getInputsNames(self):
        return self._input_name

    def getOutputsNames(self):
        return self._output_name

    # seters
    def setInputNames(self, input_names):
        if ((input_names is None) or (self._control_dimension == len(input_names))):
            self._input_name = input_names
        else:
            raise Exception("Number of input names different than control inputs.")

    def setOutputNames(self, output_names):
        if ((output_names is None) or (self._output_dimension == len(output_names))):
            self._output_name = output_names
        else:
            raise Exception("Number of output names different than outputs number.")

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
