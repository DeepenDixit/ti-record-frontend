from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    """

    APP_NAME: str = Field(default="voice-automation")
    APP_DESCRIPTION: str = Field(default="Record Filter Application Frontend")
    APP_ENVIRONMENT: str = Field(default="local")
    APP_DEBUG: bool = Field(default=True)

    APP_LOGGER_NAME: str = Field(default="VOICE_AUTOMATION")
    APP_LOG_LEVEL: str = Field(default="DEBUG")

    FLASK_SECRET_KEY: str = Field(default="")

    DEFAULT_APP_USER: str = Field(default="admin")
    DEFAULT_APP_PASSWORD: str = Field(default="admin")

    BACKEND_API_URL: str = Field(default="http://localhost:8080/filterRecords/fromJson")
    BACKEND_API_TOKEN: str = Field(default="")

    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=".env", extra="allow", env_file_encoding="utf-8"
    )


settings = Settings()
