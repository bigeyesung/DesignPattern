class Component():
   def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component