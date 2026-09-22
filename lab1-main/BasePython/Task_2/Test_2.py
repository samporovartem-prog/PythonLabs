import unittest
import Main_2



class MyTest(unittest.TestCase):

    def test_1(self):
        data = '12345'
        result = Main_2.F(data)

        self.assertEqual(result, True)

    def test_2(self):
        data = '123455'
        result = Main_2.F(data)

        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()