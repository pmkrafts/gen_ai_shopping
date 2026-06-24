.PHONY: test run lint format

test:
	python -m pytest

run:
	python main.py

debug:
	python main.py --debug

lint:
	ruff check .

format:
	ruff format .
