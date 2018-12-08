import unittest

class TestLTISystem(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_decrement(self):
        self.assertEqual(3, 4)

if __name__ == '__main__':
    unittest.main()