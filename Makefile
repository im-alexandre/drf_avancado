build_container:
	docker-compose build

build:
	docker exec api_app python3 manage.py migrate --noinput
	docker exec api_app python3 manage.py collectstatic --noinput --clear

collectstatic:
	docker exec -it api_app python3 manage.py collectstatic

run:
	docker-compose down
	docker-compose up

up:
	docker-compose down
	docker-compose up -d

logs:
	docker-compose logs -f --tail 100

down:
	docker-compose down

inspect:
	docker exec -it api_app /bin/bash

makemigrations:
	docker exec -it api_app python3 manage.py makemigrations api_app
