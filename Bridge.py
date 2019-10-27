from abc import ABC, abstractmethod

class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation


    def operation(self) -> str:
            return self.implementation.operation_implementation()

class ExtendedAbstraction(Abstraction):

    def operation(self) -> str:
        return self.implementation.operation_implementation()

class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass