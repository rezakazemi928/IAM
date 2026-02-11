from dataclasses import dataclass
from app.application.ports.roles_repo import RolesRepository
from app.domain.errors import RoleNotFound
from app.domain.roles import RoleDomain

@dataclass(frozen=True)
class RolesByNameQuery:
    name: str


class FetchRolesByNameUseCase:
    def __init__(self, rolesRepo: RolesRepository):
        self._roles = rolesRepo
        
    
    async def get_roles_by_name(self, query: RolesByNameQuery) -> RoleDomain:
        role = await self._roles.get_by_name(query.name)
        if role is None:
            raise RoleNotFound(f"role cannot be found with name {query.name}")
        return role