from fastapi import FastAPI
from sqlalchemy import text
from contextlib import asynccontextmanager

from app.infrastructure.db.session import engine
from app.core.config import settings
from app.interfaces.http.routers import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
        
    yield
    
    await engine.dispose()

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
app.include_router(auth.router, prefix="/auth", tags="auth")


