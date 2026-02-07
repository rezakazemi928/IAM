from typing import Optional
from pydantic import BaseModel


class RegisterClientRequest(BaseModel):
    account_id: str
    role_id: str
    password: Optional[str]
    phone: str
    

class RegisterResponse(BaseModel):
    account_id: str
