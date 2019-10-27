from abc import ABC, abstractmethod

class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation