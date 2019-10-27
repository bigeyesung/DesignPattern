class Target():

    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):

    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
    
    def request(self):
        return self.adaptee.specific_request()[::-1]

def client_code(target: Target):
    print(target.request(), end="")

if __name__ == "__main__":
    target = Target()
    client_code(target)
    print("\n")

    daptee = Adaptee()
    print("test")
    adaptee.specific_request()