# python-lib-template

A template project for Python 3.11 CLI projects which includes:

- [poetry](https://python-poetry.org/) for dependency management and build support
- [pytest](https://docs.pytest.org/)
- [black](https://pypi.org/project/black/)
- [isort](https://pypi.org/project/isort/)

## Development Environment Quickstart

```shell
# install dependencies 
poetry install

# run tests
poetry run pytest
```

## Using the Template

* clone the repository for your specific project `git clone <url> <your project name>`
* rename the toplevel namespace and package directories
* update pyproject.toml to reflect project naming as appropriate
* update logging.yaml to utilize the project's namespace/packaging as appropriate
