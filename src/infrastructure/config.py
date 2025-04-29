from pathlib import Path
from typing import Self

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

class Settings(BaseSettings):
    # Настройки проекта
    project_name: str = "LiteStar CRUD basic"
    version: str = "v1.0.0"

    # Параметры базы данных
    POSTGRES_DSN: str | None = None
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    PG_DATABASE: str

    # Настройки рабочих директорий проекта
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @model_validator(mode='after')
    def compose_pg_dsn(self) -> Self:
        self.POSTGRES_DSN = (
            f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}"
            f"@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DATABASE}"
        )
        return self

settings = Settings()
