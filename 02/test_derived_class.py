import unittest
from derived_class import DerivedClass

class TestDerivedClass(unittest.TestCase):
    def test_derived_class(self):
        instance = DerivedClass(4, 5, 6, 7)
        self.assertEqual(instance.prop1, 4)
        self.assertEqual(instance.prop2, 5)
        self.assertEqual(instance.prop3, 6)
        self.assertEqual(instance.derived_prop, 7)
        self.assertIsNone(DerivedClass.empty_classmethod(instance))
        self.assertIsNone(instance.empty_instance_method())

if __name__ == '__main__':
    unittest.main()
