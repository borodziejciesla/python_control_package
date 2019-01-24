import unittest
import source.lti_analysis
from  source.StateSpace import StateSpace
from  source.TransferFunction import TransferFunction
import numpy as np

class testAnalysis(unittest.TestCase):

    def test_eigenvalues_state_space(self):
        A = np.array([[1, 2], [0, 1]])
        B = np.array([[0], [1]])
        C = np.transpose(np.array([[1], [0]]))
        D = np.array([1])

        obj = StateSpace(A, B, C ,D)
        eig = source.lti_analysis.eigenvalues(obj)

        ref = np.array([1, 1])

        self.assertEqual(np.all(ref == eig), True)


    def test_eigenvalues_transfer_function(self):
        obj = TransferFunction([1], [1, 2])

        eig = source.lti_analysis.eigenvalues(obj)

        ref = np.array([-2])

        self.assertEqual(np.all(ref == eig), True)

if __name__ == '__main__':
    unittest.main()