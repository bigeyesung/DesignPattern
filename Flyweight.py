import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
            s = json.dumps(self._shared_state)
            u = json.dumps(unique_state)
            print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")

class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
            for state in initial_flyweights:
                self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight: