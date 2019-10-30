from typing import Optional
class SingletonMeta(type):
    _instance: Optional[Singleton] = None