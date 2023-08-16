from flask import render_template, g, request, current_app as app

def handle_404(e):
    potential_lang_code = request.path.split('/')[1]
    g.lang_code = potential_lang_code if potential_lang_code in app.config["LANGUAGES"] else 'en'
    return render_template("404.html", lang_code=g.lang_code), 404

# this will also capture all unexpected errors
def handle_500(HTTPException):
    return render_template("error.html", lang_code=request.path.split('/')[1]), 500



