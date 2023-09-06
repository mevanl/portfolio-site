from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")


@views.route('/projects')
def projects():
    return "<p>My Projects:</p>"


@views.route('/about')
def about_me():
    return "<h1>About Evan.</h1>"
