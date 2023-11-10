import unittest
import list_comprehension

class TestListComprehension(unittest.TestCase):
    def test_list_comprehension(self):
        result = list_comprehension.even_integers
        self.assertEqual(result, [2, 4, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()
