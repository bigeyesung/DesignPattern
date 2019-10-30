from typing import Optional
class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton: