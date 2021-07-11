from hashlib import pbkdf2_hmac
from flask import render_template, request, abort
from repositories import UserRepository
from forms import RegisterForm, LoginForm
from flask_login import login_user


def login():
        # 1. get the repository
        # 2. get user by username
        # 3. validate passwords
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        crypted_password = crypt_password(form.password.data)
        repository = UserRepository()
        user = repository.get_by_username(username)
        if user.password == crypted_password:
            login_user(user)
        else:
            abort(400)

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
    password = pbkdf2_hmac('sha256',
                           password.encode('utf8'),
                           salt.encode('utf8'),
                           999
                           )
    return password.hex()

#    TODO read about pbkdf2_hmac function
