#!/usr/bin/env python3
"""module for flask application routing"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """holds configuration for language supported"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
