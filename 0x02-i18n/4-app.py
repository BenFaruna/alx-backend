#!/usr/bin/env python3
"""module for flask application routing"""
from flask import Flask, render_template, request
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
    param = request.values.get('locale')

    if param:
        if param in app.config['LANGUAGES']:
            return param

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """route for homepage"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
