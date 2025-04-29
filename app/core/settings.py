from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret: str = "12345"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
