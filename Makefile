depends_init:
	poetry install --no-interaction

env:
	touch .env
	echo "DB_NAME=tasks\n\
	DB_USER=postgres\n\
	DB_PASSWORD=postgres\n\
	DB_HOST=localhost\n\
	DB_PORT=5460\n\
	SECRET_KEY=django-insecure-*2^ugf5tyf#7x!+v$!2tz6fv0r3r$1zy!$4%j(3+qurb)7f1g" > .env

run_db:
	docker compose up -d

run_app:
	cd task_manager && python manage.py migrate && python3 manage.py runserver

stop_db:
	docker compose down -v
