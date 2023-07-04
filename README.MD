Here is the two ways to run this app:


You could use the command in the Makefile by the order:
1) make run_app - run app
2) follow to http://0.0.0.0:8000/
3) you could find swagger docs at http://0.0.0.0:8000/swagger/ 
4) make stop_app - delete container and all volumes


You also could run it by the next steps:
1) poetry install 

2) export DB_NAME=tasks USER=postgres PASSWORD=postgres HOST=localhost PORT=5460 SECRET_KEY=django-insecure-*2^ugf5tyf#7x!+v$!2tz6fv0r3r$1zy!$4%j(3+qurb)7f1g

3) Or you could create .env file and fill it with:

DB_NAME=tasks

DB_USER=postgres

DB_PASSWORD=postgres

DB_HOST=localhost

DB_PORT=5460

SECRET_KEY=django-insecure-*2^ugf5tyf#7x!+v2tz6fv0r3rzy!%j(3+qurb)7f1g

4) docker compose up -d
5) cd task_manager && python manage.py migrate && python3 manage.py runserver
6) docker compose down -v
7) CTRL + C