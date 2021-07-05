from flask import render_template


def login():
    return render_template('login.html.jinja2', hello='World', first_name='Kuba')


def register():
    return render_template('register.html.jinja2')

