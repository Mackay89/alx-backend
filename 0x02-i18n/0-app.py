#!/usr/bin/env python3
"""A simple Flask app that serves a basic webpage."""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    """
    Render the index page with a welcome message.

    Returns:
        The rendered HTML content of the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

