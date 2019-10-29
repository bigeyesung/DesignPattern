class Component():
   def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        self._component.operation()

class ConcreteDecoratorA(Decorator):

    def operation(self):
        return self.component.operation()

class ConcreteDecoratorB(Decorator):

    def operation(self):
        return ConcreteDecoratorB({self.component.operation()})

def client_code(component: Component):
    print(component.operation())

if __name__ == "__main__":
    simple = ConcreteComponent()
    print("test")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("test")
    client_code(decorator2)