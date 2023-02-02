#!/usr/bin/env python3
"""module for flask application routing"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """route for homepage"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
