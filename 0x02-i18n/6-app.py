#!/usr/bin/env python3
"""module for flask application routing"""
from typing import Union, Dict

from flask import Flask, g, render_template, request
from flask_babel import Babel, _


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
    if 'locale' in request.args:
        param = request.args.get('locale')
    elif type(get_user()) == dict and 'locale' in get_user():
        param = getattr(g, 'user', None)['locale']
    elif 'locale' in request.headers:
        param = request.headers.get('locale')
    else:
        param = None

    if param:
        if param in app.config['LANGUAGES']:
            return param

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """function returns user if ID is present, else returns None"""
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> Dict:
    """function returns user and is ran before request"""
    user = get_user()
    setattr(g, 'user', user)


@app.route('/')
def home():
    """route for homepage"""
    return render_template('6-index.html', user=getattr(g, 'user', None))


if __name__ == "__main__":
    app.run()
