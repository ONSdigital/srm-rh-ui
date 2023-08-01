run:
	pipenv run python run.py

install:
	pipenv install --dev

load_templates:
	./scripts/load_templates.sh	

build:
	docker build -t srm-rh-ui .

docker_run:
	docker run -p 9092:9092 srm-rh-ui

docker_stop:
	docker stop srm-rh-ui

flake8:
	pipenv run flake8

vulture:
	pipenv run vulture .

liniting: flake8 

test: liniting
	APP_CONFIG=TestingConfig pipenv run pytest