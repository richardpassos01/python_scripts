class BaseClass:
    def __init__(self, prop1, prop2, prop3):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3

    @classmethod
    def empty_classmethod(cls):
        pass

    def empty_instance_method(self):
        pass
