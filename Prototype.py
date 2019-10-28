from datetime import datetime
from copy import deepcopy
from typing import Any

class Prototype:

    def __init__(self) -> None:
        self._primitive = None
        self._component = None
        self._circular_reference = None