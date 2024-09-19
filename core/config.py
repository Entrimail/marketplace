from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()


class Settings(BaseSettings):
    db_url: str


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
