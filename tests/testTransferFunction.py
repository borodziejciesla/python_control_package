import unittest
from  source.TransferFunction import TransferFunction

class TestLTISystem(unittest.TestCase):

    def test_serial_connection_1(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])
        obj_ref = TransferFunction([1], [1, 4, 4])

        obj = obj_1.serialConnection(obj_2)

        self.assertEqual(obj, obj_ref)

    def test_serial_connection_negative_1(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1, 2], [1, 2])

        obj = obj_1.serialConnection(obj_2)

        self.assertEqual(obj.isValid(), False)

    def test_multiply_operator(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])
        obj_ref = TransferFunction([1], [1, 4, 4])

        obj = obj_1 * obj_2       

        self.assertEqual(obj, obj_ref)

    def test_parallel_connection_1(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])
        obj_ref = TransferFunction([2, 4], [1, 4, 4])

        obj = obj_1.parallelConnection(obj_2)

        self.assertEqual(obj, obj_ref)

    def test_add_operator(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])
        obj_ref = TransferFunction([2, 4], [1, 4, 4])

        obj = obj_1 + obj_2

        self.assertEqual(obj, obj_ref)

    def test_feedback(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])
        obj_ref = TransferFunction([1, 2], [1, 4, 5])

        obj = TransferFunction.feedback(obj_1, obj_2)

        self.assertEqual(obj, obj_ref)

    def test_input_outputs_names(self):
        obj = TransferFunction([1], [1, 2], input_name = ['Input'], output_name = ['Output'])

        self.assertEqual(obj.getInputsNames(), ['Input'])
        self.assertEqual(obj.getOutputsNames(), ['Output'])

    def test_input_outputs_names_negative(self):
        obj = TransferFunction([1], [1, 2], input_name = ['Input_1', 'Input_2'], output_name = ['Output'])

        self.assertIsNone(obj.getInputsNames())
        self.assertIsNone(obj.getOutputsNames())

if __name__ == '__main__':
    unittest.main()
    