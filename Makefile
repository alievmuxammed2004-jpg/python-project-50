install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing

lint:
	uv run ruff check .

build:
	uv build

package-install:
	uv tool install --reinstall dist/*.whl