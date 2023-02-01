#!/usr/bin/env python3
"""module for flask application routing"""
from typing import Union, Dict
import flask
from flask import Flask, render_template, request
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """holds configuration for language supported"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """gets the best locale for the user of the webpage"""
    param = request.values.get('locale')

    if param:
        if param in app.config['LANGUAGES']:
            return param

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """function returns user if ID is present, else returns None"""
    id = request.values.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> Dict:
    """function returns user and is ran before request"""
    user = get_user()
    flask.g.user = user


@app.route('/')
def home():
    """route for homepage"""
    return render_template('5-index.html', user=flask.g.get('user'))


if __name__ == "__main__":
    app.run()
