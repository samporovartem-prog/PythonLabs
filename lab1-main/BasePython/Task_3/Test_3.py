import unittest
import Main_3



class MyTest(unittest.TestCase):

    def test_1(self):
        data = 255   # 111111
        result = Main_3.F(data)

        self.assertEqual(result, 8)

    def test_2(self):
        data = 256   # 1000000
        result = Main_3.F(data)

        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()