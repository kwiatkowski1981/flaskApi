from flask import Flask
from api import authors
from controllers import login, register


app = Flask(__name__)
# api urls
app.add_url_rule('/authors', view_func=authors.index, methods=['GET'])
app.add_url_rule('/authors', view_func=authors.add, methods=['POST'])
app.add_url_rule('/authors/<author_id>', view_func=authors.delete, methods=['DELETE'])

# controllers
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])



