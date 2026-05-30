from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str | None = None
    openai_model: str = "gpt-4.1-mini"
    honeycomb_api_key: str | None = None
    honeycomb_api_url: str = "https://api.honeycomb.io/1"
    aws_region: str = "us-east-1"
    read_only_mode: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
