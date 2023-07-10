"""
main.py

The CLI application entrypoint.
"""
import argparse
from pythoncliapp.logging import configure_logging
import logging
import sys

logger = logging.getLogger(__name__)


def main(args=None):
    """
    Parses command line arguments and configures the application.
    The system arguments are passed using the `args` parameter to separate concerns and support facilitate testing.
    :param args: The command line arguments, defaults to None.
    """
    parser = argparse.ArgumentParser(
        prog="CLI Application",
        description="The CLI Application accepts arguments and does things",
    )
    parser.add_argument(
        "--logconfig",
        default=None,
        type=str,
        help="The full path to the logging configuration.",
    )
    parsed_args = parser.parse_args()

    configure_logging(parsed_args.logconfig)
    logger.info("application complete")


if __name__ == "__main__":
    main(sys.argv)
