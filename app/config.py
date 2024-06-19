from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_pwd: str
    db_usr: str
    db_host: str
    db_port: str
    db_name: str
    jwt_secret_key: str
    jwt_algo: str
    jwt_expire_minutes: int


    class Config:
        env_file = ".env"


settings = Settings()