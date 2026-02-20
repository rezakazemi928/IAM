from __future__ import annotations


from typing import Protocol, Optional
from app.interfaces.http.schemas.token import AuthTokenSchema

class TokenAuthenticationPorts(Protocol):
    async def create_access_token(data: AuthTokenSchema) -> str:
        ...
    
    async def decode_access_token(token: str) -> AuthTokenSchema:
        ...
        
    async def verify_access_token(token_data: dict) -> bool:
        ...