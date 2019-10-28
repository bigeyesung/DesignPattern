from datetime import datetime
from copy import deepcopy
from typing import Any

class Prototype:

    def __init__(self) -> None:
        self._primitive = None
        self._component = None
        self._circular_reference = None

    @property
    def primitive(self) -> Any:
        return self._primitive

    @primitive.setter
    def primitive(self, value: Any) -> None:
        self._primitive = value

    @property
    def component(self) -> object:
        return self._component

    @component.setter
    def component(self, value: object) -> None:
        self._component = value

    @property
    def circular_reference(self) -> ComponentWithBackReference:
        return self._circular_reference

    @circular_reference.setter
    def circular_reference(self, value: ComponentWithBackReference) -> None:
        self._circular_reference = value

    def clone(self) -> Prototype:
        self.component = deepcopy(self.component)

        self.circular_reference = deepcopy(self.circular_reference)
        self.circular_reference.prototype = self
        return deepcopy(self)

class ComponentWithBackReference:

    def __init__(self, prototype: Prototype):
        self._prototype = prototype

    @property
    def prototype(self) -> Prototype:
        return self._prototype