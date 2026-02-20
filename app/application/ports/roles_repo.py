from __future__ import annotations

from typing import Protocol, Optional
from app.domain.roles import RoleDomain

class RolesRepository(Protocol):
    async def get_by_id(id: int) -> Optional[RoleDomain]:
        ...
    
    async def get_by_name(name: str) -> Optional[RoleDomain]:
        ...