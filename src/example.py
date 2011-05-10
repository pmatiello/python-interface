from interface import interface, implements, method

class comestible(interface):
    eat = method()
    buy_from = method()


@implements(comestible)
class hamburger(object):
    
    def eat(self):
        pass

    def buy_from(self):
        pass