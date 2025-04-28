from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "LiteStar CRUD basic"
    version: str = "v1.0.0"
    SECRET_KEY: str = "a" * 32  # secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    POSTGRES_DSN: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/litestar"

    # Настройки рабочих директорий проекта
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()