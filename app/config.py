from dotenv import load_dotenv
import os
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

class Setting(BaseModel):
    DB_HOSTS: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @classmethod
    def from_env(cls):
        db_hosts = os.environ.get("DB_HOSTS", "localhost")
        db_port = int(os.environ.get("DB_PORT", "5432"))
        db_user = os.environ.get("DB_USER", "postgres")
        db_pass = os.environ.get("DB_PASS", "postgres")
        db_name = os.environ.get("DB_NAME", "fastapi")
        
        return cls(
            DB_HOSTS=db_hosts,
            DB_PORT=db_port,
            DB_USER=db_user,
            DB_PASS=db_pass,
            DB_NAME=db_name,
        )

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOSTS}:{self.DB_PORT}/{self.DB_NAME}"

setting = Setting.from_env()