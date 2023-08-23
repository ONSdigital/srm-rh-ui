from flask import render_template, g, request, current_app as app


def handle_404(_exception: Exception) -> tuple[str, int]:
    potential_lang_code = request.path.split('/')[1]
    g.lang_code = potential_lang_code if potential_lang_code in app.config['LANGUAGES'] else 'en'

    return render_template("error_pages/404.html", lang_code=g.lang_code), 404


# this will also capture all unexpected errors
def handle_500(_exception: Exception) -> tuple[str, int]:
    return render_template("error_pages/error.html", lang_code=request.path.split('/')[1]), 500
