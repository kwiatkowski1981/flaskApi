from hashlib import pbkdf2_hmac
from flask import render_template, request
from repositories import UserRepository
from forms import RegisterForm


def login():
    return render_template('login.html.jinja2', hello='World', first_name='Kuba')


def register():
    # 1. hash password password
    # 2. create repository
    # 3. user save method on repository
    # 4. password and salt have to be encode

    salt = 'abcdefg123456!@#$%^&'
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = pbkdf2_hmac('sha256',
                               form.password.data.encode('utf8'),
                               salt.encode('utf8'),
                               999
                               )

        repository = UserRepository()
        repository.save(username, password)

        print('Added a new user.')
    return render_template('register.html.jinja2', form=form)

#    TODO ewad about pbkdf2_hmac function
