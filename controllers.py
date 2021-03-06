from hashlib import pbkdf2_hmac
from flask import render_template, request, abort, redirect
from repositories import UserRepository
from forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required


def login():
        # 1. get the repository
        # 2. get user by username
        # 3. validate passwords
        # TODO read about "oauth", 'json web token to secure API

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        crypted_password = crypt_password(form.password.data)
        repository = UserRepository()
        user = repository.get_by_username(username)
        if user.password == crypted_password:
            login_user(user)
            return redirect('/home')   # after log in redirect user to home site
        else:
            abort(400)

    return render_template('login.html.jinja2', form=form)


def logout():
    logout_user()
    return redirect('/login')


@login_required
def home():
    return render_template('home.html.jinja2')


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
