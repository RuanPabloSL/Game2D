

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entity import Entity


class EntityFactory:

    def get_entity(self, entity_type: str) -> Entity:
        pass
