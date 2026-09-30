install:
	poetry install

test:
	poetry run pytest --cov=gendiff

lint:
	poetry run flake8 gendiff

.PHONY: install test lint

build:
	uv build

package-install:
	uv tool install --reinstall dist/*.whl