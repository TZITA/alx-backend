#!/usr/bin/env python3
"""Flask babel babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    req_locale = request.args.get('locale')
    if req_locale and req_locale in '4-app.Config.LANGUAGES':
        return req_locale
    return request.accept_languages.best_match('4-app.Config.LANGUAGES')


@app.route("/")
def home() -> str:
    """return 1-index.html"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run()
