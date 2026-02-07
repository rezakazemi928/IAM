from __future__ import annotations

from datetime import datetime, timezone
from app.domain.account_status import AccountStatus
from app.infrastructure.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime


class AccountORM(Base):
    __tablename__ = "accounts"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, unique=True)
    client_identifier: Mapped[str] = mapped_column(String)
    status:AccountStatus = mapped_column(String)
    role_id: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    token_key: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=True)
    updated_at: datetime = mapped_column(DateTime, default=datetime.now(timezone.utc))
    created_at: datetime = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
