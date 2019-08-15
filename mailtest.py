from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
yemail = input("email: ")
ypass = input("pass: ")
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":yemail,
    "MAIL_PASSWORD": ypass
}

app.config.update(mail_settings)
mail = Mail(app)

print("whats yee email?")
email=input()
sub=input('subject: ')
print("body")
message=input()
for i in range(10):
    if __name__ == '__main__':
        with app.app_context():
            msg = Message(subject=sub,
                          sender=yemail,
                          recipients=['jeffthefreshavocado@gmail.com',email],
                          body=message)
            mail.send(msg)

