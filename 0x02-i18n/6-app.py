def get_locale() -> str:
    """
    Determine the best match for the locale based on the following priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    
    # 2. Locale from user settings
    user = getattr(g, 'user', None)
    if user and user.get('locale') in Config.LANGUAGES:
        return user['locale']
    
    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

