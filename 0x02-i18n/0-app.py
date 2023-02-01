#!/usr/bin/env python3
"""module for flask application routing"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """route for homepage"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
