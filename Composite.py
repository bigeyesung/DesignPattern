from abc import ABC, abstractmethod
from typing import List

class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent