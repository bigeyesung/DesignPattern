from abc import ABC, abstractmethod
from typing import List

class Component(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):

    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return '+'.join(results)

def client_code(component: Component):
    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")
if __name__ == "__main__":
    simple = Leaf()
    print("test componenet")
    client_code(simple)
    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("client tree:")
    client_code(tree)
    print("\n")

    print("client check tree")
    client_code2(tree, simple)