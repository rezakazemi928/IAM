from __future__ import annotations

from datetime import datetime, timezone
from app.domain.account_status import AccountStatus
from app.infrastructure.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Enum, ForeignKey, Integer


class AccountORM(Base):
    __tablename__ = "accounts"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, unique=True)
    client_identifier: Mapped[str] = mapped_column(String)
    status: Mapped[AccountStatus] = mapped_column(Enum(AccountStatus))
    role_id_int: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    role: Mapped["RoleORM"] = relationship(back_populates="accounts")
    phone: Mapped[str] = mapped_column(String)
    token_key: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
