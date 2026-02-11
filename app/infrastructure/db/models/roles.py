from __future__ import annotations

from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, Integer
from app.infrastructure.db.base import Base

class RoleORM(Base):
    __tablename__="roles"
    
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    accounts: Mapped[list["AccountORM"]] = relationship(back_populates="role")
    
