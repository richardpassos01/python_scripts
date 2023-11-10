import unittest
import next_function

class TestNextFunction(unittest.TestCase):
    def test_next_function(self):
        result = next_function.result_dict
        self.assertEqual(result, {'x': 5})


if __name__ == '__main__':
    unittest.main()
