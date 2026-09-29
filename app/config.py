from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Task & Analytics API"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./task.db"

class Config:
    env_file = ".env"

settings = Settings()