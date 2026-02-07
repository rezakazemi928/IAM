from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timezone

from app.application.ports.account_repo import AccountRepository
from app.application.ports.otp_provider import OtpProvider
from app.domain.account import Account
from app.domain.errors import UserExists
from app.domain.account_status import AccountStatus


@dataclass(frozen=True)
class RegisterCommand:
    account_id: str
    password: Optional[str]
    phone: str


@dataclass(frozen=True)
class RegisterResult:
    account_id: str


class RegisterUseCase:
    def __init__(self, accounts: AccountRepository, otp_provider: OtpProvider):
        self._accounts = accounts
        self._otp_provider = otp_provider
    
    async def register_user(self, cmd: RegisterCommand) -> Optional[RegisterResult]:
        existing = await self._accounts.get_by_account_id(cmd.account_id)
        if existing:
            raise UserExists(f"client with account id {cmd.account_id} already exists.")
        
        otp_key = self._otp_provider.generate_secret()
        account_obj = Account(
            account_id=cmd.account_id,
            role_id=cmd.role_id,
            token_key=otp_key,
            password=cmd.password,
            create_at=datetime.now(timezone.utc),
            update_at=datetime.now(timezone.utc),
            phone=cmd.phone,
            status=AccountStatus.ACTIVE,
        )
        await self._accounts.save(account_obj)
        return RegisterResult(account_id=account_obj.account_id)
        
            
