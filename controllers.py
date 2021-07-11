from hashlib import pbkdf2_hmac
from flask import render_template, request
from repositories import UserRepository
from forms import RegisterForm, LoginForm


def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        crypted_password = crypt_password(form.password.data)
        # 1. get the repository
        repository = UserRepository()
        # 2. get user by username
        user = repository.get_by_username(username)
        # 3. validate passwords
        user['password'] == crypted_password

    return render_template('login.html.jinja2', form=form)


def register():
    # 1. hash password password
    # 2. create repository
    # 3. user save method on repository
    # 4. password and salt have to be encode
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = crypt_password(form.password.data)

        repository = UserRepository()
        repository.save(username, password)

    return render_template('register.html.jinja2', form=form)


def crypt_password(password):
    salt = 'abcdefg123456!@#$%^&'
    return pbkdf2_hmac('sha256',
                       password.encode('utf8'),
                       salt.encode('utf8'),
                       999
                       )

#    TODO ewad about pbkdf2_hmac function
