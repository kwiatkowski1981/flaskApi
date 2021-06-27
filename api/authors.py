from flask import Response, request
from db import get_connection
from json import dumps, loads


def index():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, first_name, last_name FROM authors')

    return Response(dumps(cursor.fetchall()), mimetype='application/json')


def add():
    data = loads(request.data.decode('utf-8'))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        'INSERT INTO authors(first_name, last_name) VALUES(%s, %s) RETURNING id',
        (data['first_name'], data['last_name'])
    )
    author_id = cursor.fetchone()[0]
    connection.commit()

    return Response(dumps({
        'id': author_id
    }), mimetype='application/json')


def delete():
    return 'delete'

