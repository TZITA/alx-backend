#!/usr/bin/env python3
"""Flask babel babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('2-app.Config')


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    return request.accept_language.best_match('2-app.Config.LANGUAGES')


@app.route("/")
def home() -> str:
    """return 1-index.html"""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run()
