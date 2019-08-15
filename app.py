from flask import *
from flask_bootstrap import *
from flask_moment import Moment
from datetime import datetime
from flask_mail import *
import os
app = Flask(__name__)
Bootstrap(app)
Moment(app)
print('no yeet')
app.config['SECRET_KEY'] = "SomeSecretText"
users = {"kairan.quazi@gmail.com": {'first_name': 'Kairan', 'last_name': 'Quazi', 'email': 'kairan.quazi@gmail.com',
                                    'password': "@Kairan69!"}}
session = {}
print('yeey')
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'jeffthefreshavocado',
    "MAIL_PASSWORD": 'chickennuggets'
}
app.config.update(mail_settings)

mail = Mail(app)


@app.route('/', methods=['POST', 'GET'])
def registration():
    print(users)
    return render_template('registration.html', current_time=datetime.utcnow())
    # return 'wut'


@app.route('/registeruser', methods=['GET', 'POST'])
def register():
    first_name = request.form['first_name']

    last_name = request.form['last_name']

    email = request.form['email']

    password = request.form['password']

    if email in users:
        flash('User registered already, please login')
        return render_template('registration.html', current_time=datetime.utcnow())
    else:
        users[email] = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password}
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')


@app.route('/loginuser', methods=['GET', 'POST'])
def loginuser():
    email = request.form['email']

    password = request.form['password']

    if email not in users:
        flash('Please register')
        return redirect('/invalid')

    elif users[email]['password'] == password:
        with app.app_context():
            msg = Message(subject="Hello",
                          sender='jeffthefreshavocado@gmail.com',
                          recipients=['jeffthefreshavocado@gmail.com', email],
                          body="Hiiiii, this is Kairan. My Discord server is https://discord.gg/QetKWzc")
            mail.send(msg)
        session['user'] = users[email]
        first_name = session['user']['first_name']
        return redirect('/home')
    else:
        flash('wrong password')
        return redirect('/login')


@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('displaycontent.html', current_time=datetime.utcnow())


@app.route('/invalid')
def invalid():
    return render_template('invalid.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():

    del session['user']

    return redirect('/login')


@app.errorhandler(404)
def page_not_found(e):

    return render_template('error404.html', error=e, type=404), 404


@app.route("/registration")
def yaaaaaa():
    return redirect('/')


@app.errorhandler(400)
def bad_request(e):
    return render_template('error400.html', error=e, type=400), 400


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error500.html', error=e, type=500), 500


@app.route("/exit")
def exit():
    exit()


if __name__ == '__main__':
    app.run(debug=True)
