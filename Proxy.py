from abc import ABC, abstractmethod
class Subject(ABC):

    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):

    def request(self):
        print("test")

class Proxy(Subject):

    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("test")
        return True

    def log_access(self):
        print("test")

def client_code(subject: Subject):
    subject.request()

if __name__ == "__main__":

    print("test1")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("test2")
    proxy = Proxy(real_subject)
    client_code(proxy)