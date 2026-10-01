import unittest
import Main_1
import numpy as np


class MyTest(unittest.TestCase):

    def test_1(self):
        X = [
            np.array([[1, 0],
                      [0, 1]])
        ]
        V = [
            np.array([1, 1])
        ]
        ansver = [[1, 1],
                  [1, 1]]

        result = Main_1.sum_prod(X, V)
        print(result)

        self.assertEqual(result, ansver)


if __name__ == '__main__':
    unittest.main()