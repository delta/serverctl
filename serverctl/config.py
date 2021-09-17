"""
Contains the global configuration for the API.
(Modify the .env file to change the values)
"""

import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(dotenv_path="../.env")


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Class for global settings"""

    # Database settings
    postgres_user: Optional[str] = os.getenv("POSTGRES_USER")
    postgres_password: Optional[str] = os.getenv("POSTGRES_PASSWORD")
    postgres_host: Optional[str] = os.getenv("POSTGRES_HOST")
    postgres_port: Optional[str] = os.getenv("POSTGRES_PORT", "5432")
    postgres_db: Optional[str] = os.getenv("POSTGRES_DB")
    database_url = (
        f"postgresql://{postgres_user}:{postgres_password}@"
        f"{postgres_host}:{postgres_port}/{postgres_db}"
    ) if os.getenv("ENVIRONMENT") in ["dev", "prod"] \
        else "sqlite:///./.test.db"


settings = Settings()
