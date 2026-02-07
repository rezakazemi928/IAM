from __future__ import annotations

import hashlib
import secrets

from app.application.ports.password_hasher import PasswordHasher


class Pbkdf2PasswordHasher(PasswordHasher):
    def __init__(self, iterations: int = 200_000):
        self._iterations = iterations

    def hash_password(self, password: str) -> str:
        salt = secrets.token_bytes(16)
        derived = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            self._iterations,
        )
        return f"pbkdf2_sha256${self._iterations}${salt.hex()}${derived.hex()}"
