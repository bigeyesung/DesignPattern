from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass