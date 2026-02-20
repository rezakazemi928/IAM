from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuthTokenSchema(BaseModel):
    account_id: str
    createdAt: datetime
    expire_time: Optional[float] = None