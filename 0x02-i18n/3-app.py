#!/usr/bin/env python3
"""Flask babel babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    acc_lang = request.accept_languages
    best_match_lang = acc_lang.best_match(Config.Languages)

    return best_match_lang


@app.route("/")
def home():
    """return 1-index.html"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run()
