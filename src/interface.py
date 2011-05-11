from inspect import getargspec


class interface(object):
    pass


class method(object):
    def __init__(self, args=None, varargs=None, keywords=None, defaults=0):
        self.args = args or []
        self.varargs = varargs
        self.keywords = keywords
        self.defaults = defaults


class implements(object):
    
    def __init__(self, interface):
        self.interface = interface
    
    def __call__(self, clazz):
        methods = [each for each in dir(self.interface) if self._is_method(each)]
        for each in methods:
            self._assert_implements(clazz, each)
    
    def _is_method(self, name):
        try:
            return type(self._attribute(self.interface, name)) == method
        except:
            False

    def _assert_implements(self, clazz, method_name):
        self._assert_method_presence(clazz, method_name)
        contract = self._attribute(self.interface, method_name)
        method_impl = getargspec(self._attribute(clazz, method_name))
        self._assert_method_arguments(contract, method_impl)
        self._assert_method_varargs(contract, method_impl)
        self._assert_method_keyword_args(contract, method_impl)
        self._assert_method_default_args(contract, method_impl)

    def _assert_method_presence(self, clazz, method_name):
        assert method_name in dir(clazz)
    
    def _assert_method_arguments(self, contract, method_impl):
        assert contract.args == method_impl.args
        
    def _assert_method_varargs(self, contract, method_impl):
        assert contract.varargs == method_impl.varargs

    def _assert_method_keyword_args(self, contract, method_impl):
        assert contract.keywords == method_impl.keywords

    def _assert_method_default_args(self, contract, method_impl):
        if (method_impl.defaults is None):
            assert contract.defaults == 0
        else:
            assert contract.defaults == len(method_impl.defaults)

    def _attribute(self, clazz, attribute):
        return object.__getattribute__(clazz, attribute)