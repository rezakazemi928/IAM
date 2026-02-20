from __future__ import annotations

from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError
from app.application.ports.token_auth import TokenAuthenticationPorts
from app.interfaces.http.schemas.token import AuthTokenSchema
from app.core.config import settings


class TokenAuthentication(TokenAuthenticationPorts):
    def __init__(self):
        self._secret = settings.JWT_SECRET
        self._algorithm = settings.JWT_ALGORITHM
        self._expire_time = timedelta(minutes=settings.JWT_ACCESS_TTL_MIN) + datetime.now(timezone.utc)
        
    
    async def create_access_token(self, data: AuthTokenSchema) -> str:
        access_token_data = data.model_dump()
        access_token_data.update(
            {
                "expire_time": self._expire_time.isoformat()
            }
        )
        try:
            access_token = jwt.encode(
            data.model_dump(),
            self._secret,
            self._algorithm,
        )
        except JWTError as e:
            print(f"error in creating access token: {e}")
            #TODO raise an error
        
        return access_token
    
    async def decode_access_token(self, token: str):
        try:
            token_data = jwt.decode(
                token=token,
                algorithms=self._algorithm,
                key=self._secret,
            )
        except JWTError as e:
            print(f"error in decoding the error: {e}")
            #TODO raise an error
        
        return token_data
    
    async def verify_access_token(self, token_data: AuthTokenSchema):
        current_ime = datetime.now(timezone.utc)
        expires_time = datetime.fromisoformat(token_data["expire_time"])
        if expires_time > current_ime:
            print("Token has been expired")
            raise ExpiredSignatureError()
        
