import unittest
import Main_8



class MyTest(unittest.TestCase):

    def test_1(self):
        result = Main_8.F(123123)

        self.assertEqual(result, True)

    def test_2(self):
            result = Main_8.F(123129)
    
            self.assertEqual(result, False)

    def test_3(self):
            result = Main_8.F(15951)
    
            self.assertEqual(result, True)
    
    def test_4(self):
            result = Main_8.F(15952)
    
            self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()