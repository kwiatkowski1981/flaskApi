from flask import render_template, request
from forms import RegisterForm


def login():
    return render_template('login.html.jinja2', hello='World', first_name='Kuba')


def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        print('Added a new user.')
    return render_template('register.html.jinja2', form=form)
