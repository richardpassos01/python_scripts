import unittest
from base_class import BaseClass

class TestBaseClass(unittest.TestCase):
    def test_base_class(self):
        instance = BaseClass(1, 2, 3)
        self.assertEqual(instance.prop1, 1)
        self.assertEqual(instance.prop2, 2)
        self.assertEqual(instance.prop3, 3)
        self.assertIsNone(BaseClass.empty_classmethod())
        self.assertIsNone(instance.empty_instance_method())

if __name__ == '__main__':
    unittest.main()
