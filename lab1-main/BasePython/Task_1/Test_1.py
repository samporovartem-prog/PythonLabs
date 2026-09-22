import unittest
import Main_1



class MyTest(unittest.TestCase):

    def test_1(self):
        data = 'qwertyuiopasdfghjklzxcvbnm' # Все буквы
        result = Main_1.F(data)

        self.assertEqual(result, 5)

    def test_2(self):
        data = 'AaEeIiOoUu'
        result = Main_1.F(data)

        self.assertEqual(result, 10)



if __name__ == '__main__':
    unittest.main()