from flask import render_template
from forms import RegisterForm


def login():
    return render_template('login.html.jinja2', hello='World', first_name='Kuba')


def register():
    form = RegisterForm()
    return render_template('register.html.jinja2', form=form)
