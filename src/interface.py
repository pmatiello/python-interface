from inspect import getargspec

class interface(object):
    pass

class method(object):
    def __init__(self, args=None, varargs=None, keywords=None):
        self.args = args or []
        self.varargs = varargs
        self.keywords = keywords

class implements(object):
    
    def __init__(self, interface):
        self.interface = interface
    
    def __call__(self, clazz):
        target = dir(clazz)
        methods = [each for each in dir(self.interface) if self._is_method(each)]
        for each in methods:
            assert each in target
            iface_spec = self._attribute(self.interface, each)
            impl_spec = getargspec(self._attribute(clazz, each))
            assert iface_spec.args == impl_spec.args
            assert iface_spec.varargs == impl_spec.varargs
            assert iface_spec.keywords == impl_spec.keywords
            

    def _is_method(self, name):
        try:
            return type(self._attribute(self.interface, name)) == method
        except:
            False
    
    def _attribute(self, clazz, attribute):
        return object.__getattribute__(clazz, attribute)