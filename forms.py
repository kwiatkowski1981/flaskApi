from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    username = StringField('username: ', [validators.length(min=5)])
    password = PasswordField('password: ', [
        validators.length(min=8),
        validators.EqualTo('password_repeat')
    ])
    password_repeat = PasswordField('repeat password: ')


