from interface import interface, implements, method


class comestible(interface):
    eat = method(['self'])
    buy_from = method(['self', 'supermarket'])
    mix_with = method(['self'], varargs='ingredients')
    cook_with = method(['self'], keywords='ingredients')
    cook = method(['self', 'temperature'], defaults=1)


@implements(comestible)
class hamburger(object):
    
    def eat(self):
        pass

    def buy_from(self, supermarket):
        pass
    
    def mix_with(self, *ingredients):
        pass
    
    def cook_with(self, **ingredients):
        pass
    
    def cook(self, temperature=100):
        pass

print hamburger()