from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    frontend_origin: str = "http://localhost:3000"
    vector_db_url: str = "http://vector-db:6333"
    vision_service_url: str = "http://vision-service:8100"
    agent_orchestrator_url: str = "http://agent-orchestrator:8200"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
