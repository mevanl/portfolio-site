from flask import Flask


def build_site():
    site = Flask(__name__)
    site.config['SECRET_KEY'] = '04/15/23'

    from .views import views
    site.register_blueprint(views, url_prefix='/')

    return site
