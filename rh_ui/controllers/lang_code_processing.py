from flask import g


def setup_lang_code_processing(blueprint):
    @blueprint.url_defaults
    def add_language_code(endpoint, values):
        values.setdefault('lang_code', g.lang_code)

    @blueprint.url_value_preprocessor
    def pull_lang_code(endpoint, values):
        g.lang_code = values.pop('lang_code')
