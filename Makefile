setup:
	python -m pip install --upgrade pip
	python -m pip install -e .
	python -m pip install -r requirements.txt

test:
	pytest

format:
	black src tests

lint:
	ruff check src tests

run:
	python -m gis_starter.main
