import unittest
from  source.StateSpace import StateSpace
import numpy as np

class TestLTISystem(unittest.TestCase):

    def test_serial_connection_1(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        A_ref = np.array([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 2], [1, 0, 0, 1]])
        B_ref = np.array([[0], [1], [0], [1]])
        C_ref = np.transpose(np.array([[1], [0], [1], [0]]))
        D_ref = np.array([1])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)
        obj_ref = StateSpace(A_ref, B_ref, C_ref, D_ref)

        obj = obj_1.serialConnection(obj_2)

        self.assertEqual(obj, obj_ref)

    def test_serial_connection_negative_1(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0, 1], [1, 0]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([[1], [0]])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)

        obj = obj_1.serialConnection(obj_2)

        self.assertEqual(obj.isValid(), False)

    def test_multiply_operator(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        A_ref = np.array([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 2], [1, 0, 0, 1]])
        B_ref = np.array([[0], [1], [0], [1]])
        C_ref = np.transpose(np.array([[1], [0], [1], [0]]))
        D_ref = np.array([1])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)
        obj_ref = StateSpace(A_ref, B_ref, C_ref, D_ref)

        obj = obj_1 * obj_2       

        self.assertEqual(obj, obj_ref)

    def test_multiply_operator_negative(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1, 0], [0, 1]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)

        obj = obj_1 * obj_2       

        self.assertEqual(obj.isValid(), False)

    def test_parallel_connection_1(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        A_ref = np.array([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 2], [0, 0, 0, 1]])
        B_ref = np.array([[0], [1], [0], [1]])
        C_ref = np.transpose(np.array([[1], [0], [1], [0]]))
        D_ref = np.array([2])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)
        obj_ref = StateSpace(A_ref, B_ref, C_ref, D_ref)

        obj = obj_1.parallelConnection(obj_2)

        self.assertEqual(obj, obj_ref)

    def test_parallel_connection_negative_1(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0, 1], [1, 0]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)

        obj = obj_1.parallelConnection(obj_2)

        self.assertEqual(obj.isValid(), False)

    def test_add_operator(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        A_ref = np.array([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 2], [0, 0, 0, 1]])
        B_ref = np.array([[0], [1], [0], [1]])
        C_ref = np.transpose(np.array([[1], [0], [1], [0]]))
        D_ref = np.array([2])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)
        obj_ref = StateSpace(A_ref, B_ref, C_ref, D_ref)

        obj = obj_1 + obj_2

        self.assertEqual(obj, obj_ref)

    def test_add_operator_negative(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0, 0], [1, 1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)

        obj = obj_1 + obj_2

        self.assertEqual(obj.isValid(), False)

    def test_feedback(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0], [1]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        A_ref = np.array([[1, 2, 0, 0], [0, 1, -1, 0], [0, 0, 1, 2], [1, 0, 0, 1]])
        B_ref = np.array([[0], [1], [0], [0]])
        C_ref = np.transpose(np.array([[1], [0], [0], [0]]))
        D_ref = np.array([0])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)
        obj_ref = StateSpace(A_ref, B_ref, C_ref, D_ref)

        obj = StateSpace.feedback(obj_1, obj_2)

        self.assertEqual(obj, obj_ref)

    def test_feedback_negative(self):
        A1 = np.array([[1, 2], [0, 1]])
        B1 = np.array([[0, 1], [1, 0]])
        C1 = np.transpose(np.array([[1], [0]]))
        D1 = np.array([1])

        A2 = np.array([[1, 2], [0, 1]])
        B2 = np.array([[0], [1]])
        C2 = np.transpose(np.array([[1], [0]]))
        D2 = np.array([1])

        obj_1 = StateSpace(A1, B1, C1, D1)
        obj_2 = StateSpace(A2, B2, C2, D2)

        obj = StateSpace.feedback(obj_1, obj_2)

        self.assertEqual(obj.isValid(), False)

    def test_matrix_verivication_positive(self):
        A = np.array([[1, 2], [0, 1]])
        B = np.array([[0], [1]])
        C = np.transpose(np.array([[1], [0]]))
        D = np.array([1])

        obj = StateSpace(A, B, C, D)

        self.assertEqual(obj.isValid(), True)

    def test_matrix_verivication_negative_1(self):
        A = np.array([[1], [0]])
        B = np.array([[0], [1]])
        C = np.transpose(np.array([[1], [0]]))
        D = np.array([1])

        obj = StateSpace(A, B, C, D)

        self.assertEqual(obj.isValid(), False)

    def test_matrix_verivication_negative_2(self):
        A = np.array([[1, 2], [0, 1]])
        B = np.array([1])
        C = np.transpose(np.array([[1], [0]]))
        D = np.array([1])

        obj = StateSpace(A, B, C, D)

        self.assertEqual(obj.isValid(), False)

    def test_matrix_verivication_negative_3(self):
        A = np.array([[1], [0]])
        B = np.array([[0], [1]])
        C = np.transpose(np.array([1]))
        D = np.array([1])

        obj = StateSpace(A, B, C, D)

        self.assertEqual(obj.isValid(), False)

    def test_input_outputs_names(self):
        A = np.array([[1, 2], [0, 1]])
        B = np.array([[0], [1]])
        C = np.transpose(np.array([[1], [0]]))
        D = np.array([1])

        obj = StateSpace(A, B, C, D, input_name = ['Input'], output_name = ['Output'])

        self.assertEqual(obj.getInputsNames(), ['Input'])
        self.assertEqual(obj.getOutputsNames(), ['Output'])

    def test_input_outputs_names_negative(self):
        A = np.array([[1, 2], [0, 1]])
        B = np.array([[0], [1]])
        C = np.transpose(np.array([[1], [0]]))
        D = np.array([1])

        obj = StateSpace(A, B, C, D, input_name = ['Input_1', 'Input_2'], output_name = ['Output'])

        self.assertIsNone(obj.getInputsNames())
        self.assertIsNone(obj.getOutputsNames())

if __name__ == '__main__':
    unittest.main()