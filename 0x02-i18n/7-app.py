#!/usr/bin/env python3
"""
A Basic Flask application with user login mock and timezone support
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
import pytz

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)

def get_locale() -> str:
    """
    Gets locale from request object, user settings, or default
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    user = getattr(g, 'user', None)
    if user and user.get('locale') in Config.LANGUAGES:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """
    Gets user from the mock database using the login_as parameter
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """
    Executed before each request to set the user globally, set the locale,
    and handle timezone
    """
    g.user = get_user()
    g.locale = get_locale()
    g.timezone = get_timezone()

def get_timezone() -> str:
    """
    Gets timezone from request object, user settings, or default
    """
    timezone = request.args.get('timezone', '').strip()
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass
    user = getattr(g, 'user', None)
    if user and user.get('timezone'):
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except pytz.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the home page with user-specific greetings
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)

