class Target():

    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee