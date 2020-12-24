class Component:
    def __init__(self, identifier):
        self.identifier = identifier

class Composite(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.components = set()
        
    def add_component(self, leaf):
        self.components.add(leaf)

    def soulmates_check(self):
        cs = [ component.identifier for component in self.components ]
        if 'you' in cs and 'I' in cs:
            print('we are soulmates')


if __name__ == "__main__":
    you = Component('you')
    me = Component('I')
    composite = Composite('Composite')
    composite.add_component(you)
    composite.add_component(me)
    composite.soulmates_check()

