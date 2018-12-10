import unittest
from  source.TransferFunction import TransferFunction

class TestLTISystem(unittest.TestCase):

    def test_serial_connection_1(self):
        obj_1 = TransferFunction([1], [1, 2])
        obj_2 = TransferFunction([1], [1, 2])

        obj = obj_1.serialConnection(obj_2)

        obj_ref = TransferFunction([2, 4], [1, 4, 4])

        self.assertEqual(obj, obj_ref)

if __name__ == '__main__':
    unittest.main()