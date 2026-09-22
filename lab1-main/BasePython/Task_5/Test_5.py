import unittest
import Main_5



class MyTest(unittest.TestCase):

    def test_1(self):
        V1 = [1, 1, 1]
        V2 = [1, 1, 1]
        result = Main_5.mse(V1, V2)

        self.assertEqual(result, 0)

    def test_2(self):
            V1 = [1, 0, 1]
            V2 = [1, 1, 0]
            result = Main_5.mse(V1, V2)
    
            self.assertEqual(round(result, 3), 0.816)



if __name__ == '__main__':
    unittest.main()