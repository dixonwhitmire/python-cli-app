"""
tests package

contains convenience functions/attributes used to support unit testing.
"""
import os

# base resource directory for "file based fixtures"
resources_directory = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "resources",
)
