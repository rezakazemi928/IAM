from __future__ import annotations

from typing import Protocol, Optional
from app.domain.account import Account


class AccountRepository(Protocol):
    async def get_by_account_id(self, account_id: str) -> Optional[Account]:
        ...
    
    async def get_by_id(self, id: str) -> Optional[Account]:
        ...
    
    async def save(self, account: Account) -> Optional[Account]:
        ...
