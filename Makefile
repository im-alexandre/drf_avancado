all:
	docker-compose up --build
build:
	docker exec api_app pip3 install --upgrade pip
	docker exec api_app pip3 install -r requirements.txt
	docker exec api_app python3 manage.py makemigrations
	docker exec api_app python3 manage.py migrate

test:
	docker exec api_app python3 manage.py test

run:
	docker-compose down
	docker-compose up

scrap:
	docker exec api_app python3 manage.py BSoup

down:
	docker-compose down

inspect:
	docker exec -it application /bin/bash