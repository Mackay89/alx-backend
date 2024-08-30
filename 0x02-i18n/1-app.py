#!/usr/bin/env python3
"""A Babel and Flask app supporting internationalization."""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configurations for language, locale, and timezone.

    LANGUAGES: Supported languages for the app.
    BABEL_DEFAULT_LOCALE: The default language/locale.
    BABEL_DEFAULT_TIMEZONE: The default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world() -> str:
    """
    Renders the index page.
    Returns:
        The rendered HTML content of the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
