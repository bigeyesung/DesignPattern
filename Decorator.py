class Component():
   def operation(self) -> str:
        pass
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"