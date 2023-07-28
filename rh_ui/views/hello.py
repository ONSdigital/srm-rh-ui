from flask import Blueprint, render_template


hello_bp = Blueprint("hello_bp", __name__, static_folder="../static", template_folder="../templates")


@hello_bp.route("/", methods=["GET"])
def hello():
    return render_template("hello.html")
