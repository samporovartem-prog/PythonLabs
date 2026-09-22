import unittest
import Main_4



class MyTest(unittest.TestCase):

    def test_1(self):
        data = 39
        result = Main_4.F(data, 0)

        self.assertEqual(result, 3)

    def test_2(self):
        data = 4
        result = Main_4.F(data, 0)

        self.assertEqual(result, 0)

    def test_3(self):
            data = 999
            result = Main_4.F(data, 0)
    
            self.assertEqual(result, 4)



if __name__ == '__main__':
    unittest.main()