from interface import interface, implements, method

class comestible(interface):
    eat = method(["self"])
    buy_from = method(["self", "supermarket"])


@implements(comestible)
class hamburger(object):
    
    def eat(self):
        pass

    def buy_from(self, supermarket):
        pass