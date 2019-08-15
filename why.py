from flask import *
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'yeet'


@app.route('/')
def index():
    flash("Hello User")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
