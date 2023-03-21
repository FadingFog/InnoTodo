from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/postgres"

    PRIVATE_SECRET_KEY: str = 'Hdpl8E4HNSYjI4YcLF2TjqgEMFaeghratyEe6lbVRVs='

    KAFKA_TOPIC: str = 'statistics'
    KAFKA_BOOTSTRAP_SERVERS: str = 'kafka:9093'

    class Config:
        env_file = ".env"


settings = Settings()
