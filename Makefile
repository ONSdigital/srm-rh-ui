load_templates:
	./load_templates.sh

install: load_templates
	pipenv install --dev

run: run_gunicorn

run_dev:
	APP_CONFIG=DevelopmentConfig pipenv run python run.py

run_gunicorn:
	pipenv run gunicorn

flake:
	pipenv run flake8 --exclude=whitelist.py

vulture:
	pipenv run vulture .

update_vulture_whitelist:
	pipenv run vulture . --make-whitelist > whitelist.py || true

lint: flake vulture

unit_test: lint
	APP_CONFIG=TestingConfig pipenv run pytest tests/unit --cov rh_ui --cov-report term-missing --cov-report xml

test: install unit_test integration_test

build: test docker_build

docker_build:
	docker build -t europe-west2-docker.pkg.dev/ssdc-rm-ci/docker/srm-rh-ui .

docker_run:
	docker run -p 9093:9092 --network=ssdcrmdockerdev_default -e APP_CONFIG=DevelopmentConfig -e RH_SVC_URL=http://rh-service:8071/ --name srm-rh-ui europe-west2-docker.pkg.dev/ssdc-rm-ci/docker/srm-rh-ui

docker_stop:
	docker stop srm-rh-ui
	docker rm srm-rh-ui

extract_translation:
	pipenv run pybabel extract -F babel.cfg -o rh_ui/translations/messages.pot .

update_welsh_translation_file:
	pipenv run pybabel init -i rh_ui/translations/messages.pot -d rh_ui/translations -l cy

compile_translations:
	pipenv run pybabel compile -d rh_ui/translations

translate:
	pipenv run pybabel extract -F babel.cfg -o rh_ui/translations/messages.pot . 		# update the .pot files basing on templates
	pipenv run pybabel update -i rh_ui/translations/messages.pot -d rh_ui/translations	# update .po files basing on .pot
	pipenv run pybabel compile -d rh_ui/translations

up:
	docker compose up -d
	bash ./tests/integration/wait_for_dependencies.sh

down:
	docker compose down

integration_test: lint up
	APP_CONFIG=TestingConfig pipenv run pytest tests/integration
	docker compose down

