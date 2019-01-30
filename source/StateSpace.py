import source.LTIObject as LTIObject
import numpy as np

class StateSpace(LTIObject.LTIObject):
    
    def __init__(self, A, B, C, D, create_empty = False, input_name = None, output_name = None):
        if (create_empty == False):
            self.__verifyMatrixDimensions(A, B, C, D)

            if self._is_valid:
                self._A = A
                self._B = B
                self._C = C
                self._D = D

                self._state_dimension = A.shape[0]
                self._control_dimension = B.shape[1]
                self._output_dimension = C.shape[0]
            else:
                self._A = []
                self._B = []
                self._C = []
                self._D = []

                self._state_dimension = []
                self._control_dimension = []
                self._output_dimension = []

                print("Invalid Matrix dimensions")
        else:
            self._is_valid = False

            self._A = []
            self._B = []
            self._C = []
            self._D = []

            self._state_dimension = []
            self._control_dimension = []
            self._output_dimension = []

        try:
            super().__init__(input_name, output_name)
        except Exception as error:
            print(error)
        except:# NameError as error:
            print("Unknown Error")

    def __verifyMatrixDimensions(self, A, B, C, D):
        if (A.size > 1):
            state_matrix_shape = A.shape
        else:
            state_matrix_shape = (1, 1)

        if (B.size > 1):
            control_matrix_shape = B.shape
        else:
            control_matrix_shape = (1, 1)

        if (C.size > 1):
            output_matrix_shape = C.shape
        else:
            output_matrix_shape = (1, 1)

        if (D.size > 1):
            direct_control_matrix_shape = D.shape
        else:
            direct_control_matrix_shape = (1, 1)

        self._is_valid = (state_matrix_shape[0] == state_matrix_shape[1]) and (state_matrix_shape[0] == control_matrix_shape[0])
        self._is_valid = self._is_valid and (output_matrix_shape[1] == state_matrix_shape[1]) and (output_matrix_shape[1] <= state_matrix_shape[0])
        self._is_valid = self._is_valid and (direct_control_matrix_shape[0] == output_matrix_shape[0]) and (direct_control_matrix_shape[1] == control_matrix_shape[1])

    # Operator == overloaded
    def __eq__(self, other):
        return (np.array_equal(self._A, other._A) and np.array_equal(self._B, other._B) and np.array_equal(self._C, other._C) and np.array_equal(self._D, other._D))

    # Convert to string
    def __str__(self):
        return 'State Matrix A:\n' + str(self._A) + '\nControl Matrix B:\n' + str(self._B) + '\nOutput Matrix C:\n' + str(self._C) + '\nDirect Control Matrix D:\n' + str(self._D)

    # Get matrices
    def getA(self):
        return self._A

    def getB(self):
        return self._B

    def getC(self):
        return self._C

    def getD(self):
        return self._D

    ## Analysis
    def eigenvalues(self):
        if self.isValid():
            eig, vec = np.linalg.eig(self._A)
            return eig
        else:
            return []

    ## Connections
    def serialConnection(self, consecutive_object):
        if StateSpace._isValidShapeForSerialConnection(self, consecutive_object):
            A1 = self._A
            B1 = self._B
            C1 = self._C
            D1 = self._D

            A2 = consecutive_object._A
            B2 = consecutive_object._B
            C2 = consecutive_object._C
            D2 = consecutive_object._D

            # Verification of matrix dimensions is needed
            z1 = np.zeros((A1.shape[0], A2.shape[1]))
            new_A = np.concatenate( (np.concatenate([A1, z1], axis = 1), np.concatenate([B2 * C1, A2], axis = 1)) )
            new_B = np.concatenate([B1, B2 * D1])
            new_C = np.concatenate([D2 * C1, C2], axis = 1)
            new_D = D2 * D1

            return StateSpace(new_A, new_B, new_C, new_D)
        else:
            return StateSpace([], [], [], [], True)

    def parallelConnection(self, consecutive_object):
        if StateSpace._isValidShapeForParallelConnection(self, consecutive_object):
            A1 = self._A
            B1 = self._B
            C1 = self._C
            D1 = self._D

            A2 = consecutive_object._A
            B2 = consecutive_object._B
            C2 = consecutive_object._C
            D2 = consecutive_object._D

            # Verification of matrix dimensions is needed
            z1 = np.zeros((A1.shape[0], A2.shape[1]))
            z2 = np.zeros((A2.shape[0], A1.shape[1]))
            new_A = np.concatenate( (np.concatenate([A1, z1], axis = 1), np.concatenate([z2, A2], axis = 1)) )
            new_B = np.concatenate([B1, B2])
            new_C = np.concatenate([C1, C2], axis = 1)
            new_D = D1 + D2

            return StateSpace(new_A, new_B, new_C, new_D)
        else:
            return StateSpace([], [], [], [], True)

    def feedbackConnection(self, upper_line, feedback_line):
        if StateSpace._isValidShapeForFeedbackConnection(upper_line, feedback_line):
            A1 = upper_line._A
            B1 = upper_line._B
            C1 = upper_line._C
            #D1 = upper_line._D

            A2 = feedback_line._A
            B2 = feedback_line._B
            C2 = feedback_line._C
            #D2 = feedback_line._D

            # Verification of matrix dimensions is needed
            new_A = np.concatenate( (np.concatenate([A1, -B1 * C2], axis = 1), np.concatenate([B2 * C1, A2], axis = 1)) )
            zb = np.zeros((A2.shape[0], B1.shape[1]))
            new_B = np.concatenate([B1, zb])
            zc = np.zeros((C1.shape[0], A2.shape[1]))
            new_C = np.concatenate([C1, zc], axis = 1)
            new_D = np.array([0])

            return StateSpace(new_A, new_B, new_C, new_D)
        else:
            return StateSpace([], [], [], [], True)
