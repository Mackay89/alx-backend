from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@app.route('/')
def home():
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run()

