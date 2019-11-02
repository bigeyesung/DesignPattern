from abc import ABC, abstractmethod
class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True