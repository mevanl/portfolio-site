from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")


@views.route('/resume')
def resume():
    return render_template("resume.html")


@views.route('/projects')
def projects():
    return render_template("projects.html")


@views.route('/about')
def about_me():
    return render_template("about.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")
