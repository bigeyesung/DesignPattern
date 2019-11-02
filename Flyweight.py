import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state