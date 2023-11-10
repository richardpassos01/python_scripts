import sys
import os
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, "..", "01"))

from base_class import BaseClass

class DerivedClass(BaseClass):
    def __init__(self, prop1, prop2, prop3, derived_prop):
        super().__init__(prop1, prop2, prop3)
        self.derived_prop = derived_prop

    def empty_classmethod(self):
        pass

    def empty_instance_method(self):
        pass
