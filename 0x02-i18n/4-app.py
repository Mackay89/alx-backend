#!/usr/bin/env python3
"""
A basic Flask application
"""
from flask import Flask, request, render_template
from flask_babelex import Babel


class Config:
    """
    Configuration for the Flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Render the homepage.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)

