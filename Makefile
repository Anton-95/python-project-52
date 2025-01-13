install:
	uv sync

start:
	uv run python manage.py runserver

build:
	./build.sh
