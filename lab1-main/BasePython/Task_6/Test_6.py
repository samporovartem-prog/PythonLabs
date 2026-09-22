import unittest
import Main_6



class MyTest(unittest.TestCase):

    def test_1(self):
        result = Main_6.F(86240)

        self.assertEqual(result, '(2**5)(5)(7**2)(11)')

    def test_2(self):
            result = Main_6.F(123456789)
    
            self.assertEqual(result, '(3**2)(3607)(3803)')



if __name__ == '__main__':
    unittest.main()