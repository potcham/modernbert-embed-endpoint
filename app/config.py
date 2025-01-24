from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = "nomic-ai/modernbert-embed-base"
    class Config:
        env_file = ".env"

settings = Settings()
