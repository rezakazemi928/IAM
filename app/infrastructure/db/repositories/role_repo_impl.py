from __future__ import annotations

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy import select
from app.application.ports.roles_repo import RolesRepository
from app.infrastructure.db.models.roles import RoleORM
from app.domain.roles import RoleDomain

def to_domain(orm: RoleORM) -> RoleDomain:
    if orm is not None:
        return RoleDomain(
            id=orm.id,
            name=orm.name,
            created_at=orm.created_at,
        )


class SqlAlchemyRoleRepository(RolesRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, id ) -> Optional[RoleDomain]:
        stmt = select(RoleORM).where(RoleORM.id == id)
        res = await self._session.execute(stmt)
        row = res.scalar_one_or_none()
        return to_domain(row)
    
    async def get_by_name(self, name) -> Optional[RoleDomain]:
        stmt = select(RoleORM).where(RoleORM.name == name)
        res = await self._session.execute(stmt)
        row = res.scalar_one_or_none()
        return to_domain(row)