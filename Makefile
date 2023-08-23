run:
	pipenv run python run.py

install:
	pipenv install --dev

build: unit_tests docker-build

test: install unit_tests

docker-build:
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
	pipenv run vulture . --make-whitelist > whitelist.py || true

linting: flake8 vulture

unit_tests: linting
	APP_CONFIG=TestingConfig pipenv run pytest --cov rh_ui --cov-report term-missing --cov-report xml

load_templates:
	./load_templates.sh

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