"""
logging.py

Configures logging for the CLI application.
"""
import os
import logging
import logging.config
import sys
from typing import Optional
import yaml
from yaml import YAMLError


def configure_logging(logging_config: Optional[str] = None) -> None:
    """
    Configures logging for the CLI application.
    A basic logging configuration is applied if `logging_config` is not provided or is not a valid configuration file.

    :param logging_config: The full path to the logging configuration file.
    """

    def apply_basic_config():
        """Applies a basic config for console logging"""
        logging.basicConfig(
            stream=sys.stdout,
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )

    config_path = os.path.abspath(logging_config) if logging_config else None
    print(f"config path = {config_path}")

    if config_path and os.path.exists(config_path):
        with open(logging_config, "r") as f:
            try:
                logging_config = yaml.safe_load(f)
                logging.config.dictConfig(logging_config)
                sys.stdout.write(
                    f"Loaded logging configuration from {logging_config}\n"
                )
            except YAMLError as e:
                apply_basic_config()
                sys.stderr.write(
                    f"Unable to load logging configuration from file: {e}.\n"
                )
                sys.stdout.write("Applying basic logging configuration.\n")
    else:
        sys.stdout.write(
            "Logging configuration not found. Applying basic logging configuration.\n"
        )
        apply_basic_config()
