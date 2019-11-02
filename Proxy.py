from abc import ABC, abstractmethod
class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):