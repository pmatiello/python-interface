class interface(object):
    pass

class method(object):
    def __init__(self):
        pass

class implements(object):
    
    def __init__(self, interface):
        self.interface = interface
    
    def __call__(self, clazz):
        target = dir(clazz)
        methods = [each for each in dir(self.interface) if self._is_method(each)]
        for each in methods:
            assert each in target

    def _is_method(self, name):
        try:
            return type(object.__getattribute__(self.interface, name)) == method
        except:
            False