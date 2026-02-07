from __future__ import annotations

import pyotp

from app.application.ports.otp_provider import OtpProvider


class PyOtpProvider(OtpProvider):
    def generate_secret(self) -> str:
        return pyotp.random_base32()
