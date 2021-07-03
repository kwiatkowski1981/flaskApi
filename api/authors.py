from flask import Response, request, abort
from json import dumps, loads
from repositories import AuthorsRepository


def index():
    repository = AuthorsRepository()
    return Response(dumps(repository.get_all()), mimetype='application/json')


def add():
    repository = AuthorsRepository()
    data = loads(request.data.decode('utf-8'))
    author_id = repository.save(data['first_name'], data['last_name'])

    return Response(dumps({
        'id': author_id
    }), mimetype='application/json', status=201)


def delete(author_id):
    repository = AuthorsRepository()
    author = repository.get(author_id)
    if author is None:
        abort(404)
    repository.delete(author_id)

    return Response(dumps({
        'status': 'ok',
        'author': 'usunięty'
    }), mimetype='application/json', status=200)
