
from typing import Protocol


class Entity(Protocol):

    def move(self) -> None:
        pass
