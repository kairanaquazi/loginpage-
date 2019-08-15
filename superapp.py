from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

yemail=input('what is your email? ')
password=input('what is your password?')
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": yemail,
    "MAIL_PASSWORD": password
}

app.config.update(mail_settings)
mail = Mail(app)

print("what's the email?")
email=input()

print("body")
message=input()

print('subject')
subject=input()
@app.route("/")
def mailsend():
 with app.app_context():
        msg = Message(subject=subject,
                      sender=yemail,
                      recipients=[email,yemail],
                      body=message)
        mail.send(msg)

if __name__ == '__main__':
   app.run(debug=True)
