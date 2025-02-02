install:
	uv sync

dev:
	uv run python manage.py runserver 8090

start-render:
	gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000

build:
	./build.sh

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

linter:
	uv run ruff check task_manager
