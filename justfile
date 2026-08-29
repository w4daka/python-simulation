test:
    uv run pytest

lint:
    uv run ruff check .

format:
    uv run ruff format .

typecheck:
    uv run basedpyright

cov:
    uv run pytest --cov

check: lint typecheck test
