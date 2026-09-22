import unittest
import Main_7



class MyTest(unittest.TestCase):

    def test_1(self):
        result = Main_7.pyramid(14)

        self.assertEqual(result, 3)

    def test_2(self):
        result = Main_7.pyramid(15)

        self.assertEqual(result, 'It is impossible')



if __name__ == '__main__':
    unittest.main()