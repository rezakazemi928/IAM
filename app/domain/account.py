from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.domain.account_status import AccountStatus
from app.domain.errors import UserIsNotActive

@dataclass(frozen=True)
class Account():
    account_id: str
    phone: str
    role_id: str
    token_key: str
    password: Optional[str]
    status: AccountStatus
    create_at: datetime
    update_at: datetime
    
    
    def can_authenticate(self):
        if self.status != AccountStatus.ACTIVE:
            raise UserIsNotActive(f"user with account id {self.account_id} is not active.")
    
    
    
