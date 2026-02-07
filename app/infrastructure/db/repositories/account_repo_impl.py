from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.infrastructure.db.models.account import AccountORM
from app.domain.account import Account
from app.domain.account_status import AccountStatus
from app.application.ports.account_repo import AccountRepository


def to_domain(row: AccountORM) -> Optional[Account]:
    if row is not None:
        return Account(
            account_id=row.client_identifier,
            phone=row.phone,
            role_id=row.role_id,
            token_key=row.token_key,
            password=row.password,
            status=AccountStatus(row.status),
            create_at=row.created_at,
            update_at=row.updated_at,
        )
    return None

def to_orm(entity: Account) -> AccountORM:
    return AccountORM(
        id=entity.account_id,
        client_identifier=entity.account_id,
        status=entity.status.value,
        role_id=entity.role_id,
        phone=entity.phone,
        token_key=entity.token_key,
        password=entity.password,
        created_at=entity.create_at,
        updated_at=entity.update_at,
    )

class SqlAlchemyAccountRepository(AccountRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
        
    async def get_by_id(self, id: str) -> Optional[Account]:
        stmt = select(AccountORM).where(AccountORM.id == id)
        res = await self._session.execute(stmt)
        row = res.scalar_one_or_none()
        return to_domain(row)
    
    async def get_by_account_id(self, account_id):
        stmt = select(AccountORM).where(AccountORM.client_identifier == account_id)
        res = await self._session.execute(stmt)
        row = res.scalar_one_or_none()
        return to_domain(row)
    
    async def save(self, account: Account) -> Optional[Account]:
        orm_obj = to_orm(account)
        self._session.add(orm_obj)
        await self._session.commit()
        await self._session.refresh(orm_obj)
        return to_domain(orm_obj)
