"""
settings.py

Configuration settings for the CLI application. 
Settings are supported using pydantic's Base Settings
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class CliAppSettings(BaseSettings):
    """
    The configuration settings for the CLI application.
    """

    logging_config: str = Field(
        description="The full path to the logging configuration."
    )
