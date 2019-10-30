from typing import Optional
class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):

if __name__ == "__main__":