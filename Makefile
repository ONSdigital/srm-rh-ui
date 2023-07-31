run:
	pipenv run python run.py

install:
	pipenv install

load_templates:
	./scripts/load_templates.sh	

build:
	docker build -t srm-rh-ui .

docker_run:
	docker run -p 9092:9092 srm-rh-ui

docker_stop:
	docker stop srm-rh-ui

translate:
	pipenv run pybabel extract -F babel.cfg -o rh_ui/translations/messages.pot . 		# update the .pot files basing on templates
	pipenv run pybabel update -i rh_ui/translations/messages.pot -d rh_ui/translations	# update .po files basing on .pot
	pipenv run pybabel compile -d rh_ui/translations	