# SRM Respondent Home UI
User Interface for respondents to access ONS Survey Data Collection questionnaires and services

## Installation/build
To install all dependencies and download the templates run:
```shell
make install
```

To build the docker image and run the tests:
```shell
make build
```

## Running

Once that's done, you can run the make command to run it in your terminal:
```shell
make run
```

or to run it in Pycharm, use the run template that's specified and it should work as expected.

## Translations
The site uses babel for translations.

Text to translate is marked up in html and py templates and files, then a messages.pot is build via pybabel, which collates all the text to translate into a single file.

To build/re-build the translation messages.pot use:

```
pipenv run pybabel extract -F babel.cfg -o app/translations/messages.pot .
```
    
To create a new language messages file, run the following, changing the 2 character language code at the end to the required language code. Only generate a individual language file once.

Note that this implementation includes an English translation. This is needed due to an issue with implementing pybabel with aiohttp.

```
pipenv run pybabel init -i app/translations/messages.pot -d app/translations -l cy
```

Once created, you can update the existing language messages.po files to include changes in the messages.pot by running the following. This will update ALL language files.

```
pipenv run pybabel update -i app/translations/messages.pot -d app/translations
```
    
To compile updates to the messages.po files into messages.mo (the file actually used by the site) use:

```
pipenv run pybabel compile -d app/translations
```
