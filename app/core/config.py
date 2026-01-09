from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    aws_region: str = "us-east-1"
    s3_bucket: str
    ddb_table: str = "archive_artifacts"
    log_level: str = "INFO"

settings = Settings()
