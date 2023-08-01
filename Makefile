run:
	pipenv run python run.py

install:
	pipenv install --dev

load_templates:
	./scripts/load_templates.sh	

docker_build:
	docker build -t srm-rh-ui .

docker_run:
	docker run -p 9092:9092 srm-rh-ui

docker_stop:
	docker stop srm-rh-ui

flake8:
	pipenv run flake8 --exclude=whitelist.py 

vulture:
	pipenv run vulture .

update_vulture_whitelist:
	pipenv run vulture . --make-whitelist > whitelist.py

linting: flake8 vulture

unit_tests: linting
	APP_CONFIG=TestingConfig pipenv run pytest --cov rh_ui --cov-report term-missing --cov-report xml
