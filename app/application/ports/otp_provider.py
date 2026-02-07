from __future__ import annotations

from typing import Protocol


class OtpProvider(Protocol):
    def generate_secret(self) -> str:
        ...
