from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Production FastAPI Template"
    environment: str = "local"
    secret_key: str = "change-me"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/app"
    redis_url: str = "redis://localhost:6379/0"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
