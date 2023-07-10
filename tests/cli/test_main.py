"""
test_main.py

Tests the CLI entrypoint.
"""
from pythoncliapp.cli.main import main
from tests import resources_directory
import pytest
import os


@pytest.fixture
def logging_config_path() -> str:
    """Returns a sample and valid logging configuration path"""
    return os.path.join(resources_directory, "logging.yaml")


def test_main(logging_config_path: str):
    """Tests the main entrypoint with varying parameters"""
    main(args=None)
    main(args=["--logconfig", logging_config_path])
