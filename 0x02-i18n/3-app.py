#!/usr/bin/env python3
"""A Babel and Flask app for internationalization."""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """
    Configuration for language, locale, and timezone settings.

    LANGUAGES: Supported languages for the app.
    BABEL_DEFAULT_LOCALE: Default language/locale.
    BABEL_DEFAULT_TIMEZONE: Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with the supported languages.

    Returns:
        The best-matched language from the request headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    """
    Render the index page with internationalized content.

    Returns:
        The rendered HTML content of the index page.
    """
    return render_template('2-index.html',
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
