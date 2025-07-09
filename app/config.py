from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URI: str
    MY_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()