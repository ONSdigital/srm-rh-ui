from flask import render_template, g, request
from config import BaseConfig

# how to import it from the config.py ???
LANGUAGES = ['en', 'cy']

def handle_404(e):
    potential_lang_code = request.path.split('/')[1] 
    g.lang_code = potential_lang_code if potential_lang_code in LANGUAGES else 'en'

    return render_template("404.html", lang_code=g.lang_code), 404


def handle_500(HTTPException):
    return render_template("error.html", lang_code=request.path.split('/')[1]), 500


'''
need to define a class in order for it to handle generic http exception

it would be easy if we had the global app object, but we decided we don't want that

then we can register it like that:
app.register_error_handler(error_class, handler_function)
'''
# def handle_error(e):
#     code = 500
#     if isinstance(HTTPException, e):
#         code = e.code
#     return render_template("error.html", lang_code=g.lang_code), code