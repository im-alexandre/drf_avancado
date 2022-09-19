build_container:
	docker-compose build

build:
	docker exec api_app python3 manage.py migrate --noinput

collectstatic:
	docker exec -it api_app python3 manage.py collectstatic

install:
	docker-compose down
	docker-compose up --build

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
