import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    APP_NAME: str = "iap_service"
    ENV: str = "dev"
    
    DATABASE_URL: str
    
    JWT_ISSUER: str
    JWT_AUDIENCE: str
    JWT_SECRET: str
    JWT_ACCESS_TTL_MIN: int
    JWT_REFRESH_TTL_MIN: int
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")


settings = Settings()