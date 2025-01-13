install:
	uv sync

dev:
	uv run python manage.py runserver

start-render:
	gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000

build:
	./build.sh
