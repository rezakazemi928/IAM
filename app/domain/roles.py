from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class RoleDomain:
    id: int
    name: str
    created_at: datetime
