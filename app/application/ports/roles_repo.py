from __future__ import annotations

from typing import Protocol, Optional
from app.domain.roles import Roles

class RolesRepository(Protocol):
    async def get_by_id(id: int) -> Optional[Roles]:
        ...
    
    async def get_by_name(name: str) -> Optional[Roles]:
        ...