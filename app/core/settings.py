from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret: str = "1cb890a12ce2baf434722840add76a263c1e812835985ce217bd02dc885331a8"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
