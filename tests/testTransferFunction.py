import unittest
from  source.TransferFunction import TransferFunction

class TestLTISystem(unittest.TestCase):

    def test_serial_connection_1(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])

        obj = obj_1.serialConnection(obj_2)

        obj_ref = TransferFunction([2, 4], [1, 4, 4])

        obj.printSystem()

        ref_num = obj_ref.getNumerator()
        obj_num = obj.getNumerator()

        ref_den = obj_ref.getDenumerator()
        obj_den = obj.getDenumerator()

        # Compare
        self.assertEqual(len(ref_num), len(obj_num))
        for i in range(0, len(ref_num)):
            self.assertEqual(ref_num[i], obj_num[i])

        self.assertEqual(len(ref_den), len(obj_den))
        for i in range(0, len(ref_den)):
            self.assertEqual(ref_den[i], obj_den[i])


if __name__ == '__main__':
    unittest.main()