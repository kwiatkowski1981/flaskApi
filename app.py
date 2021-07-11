from flask import Flask
from api import authors
from flask_login import LoginManager
from controllers import login, register
from repositories import UserRepository


app = Flask(__name__)
app.config['SECRET_KEY'] = '@@asdfghjkl((1232353546asdwqerxcb)$@%^*@%$&'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    repo = UserRepository()
    return repo.get_by_id(user_id)


# api urls
app.add_url_rule('/authors', view_func=authors.index, methods=['GET'])
app.add_url_rule('/authors', view_func=authors.add, methods=['POST'])
app.add_url_rule('/authors/<author_id>', view_func=authors.delete, methods=['DELETE'])

# controllers
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])



