from __future__ import annotations

from typing import Protocol


class PasswordHasher(Protocol):
    def hash_password(self, password: str) -> str:
        ...
