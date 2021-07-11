from auth import User
from psycopg2 import extras
from db import get_connection


class UserRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def map_row_to_user(self, row):
        user = User()
        user_id = row['id']
        user.username = row['username']
        user.password = row['password']
        return user

    def get_by_username(self, username):
        self.cursor.execute('SELECT id, username, password FROM users WHERE username=%s', (username,))
        return self.map_row_to_user(
            self.cursor.fetchone()
        )

    def get_by_id(self, user_id):
        self.cursor.execute('SELECT id, username, password FROM users WHERE id=%s', (user_id,))
        return self.map_row_to_user(
            self.cursor.fetchone()
        )

    def save(self, username, password):
        self.cursor.execute(
            'INSERT INTO users(username, password) VALUES(%s, %s) RETURNING id',
            (username, password)
        )
        user_id = self.cursor.fetchone()
        self.connection.commit()

        return user_id['id']


class AuthorsRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def get_all(self):
        self.cursor.execute('SELECT id, first_name, last_name FROM authors')
        return self.cursor.fetchall()

    def get(self, author_id):
        self.cursor.execute('SELECT id, first_name, last_name FROM authors WHERE id=%s', (author_id,))
        return self.cursor.fetchone()

    def save(self, first_name, last_name):
        self.cursor.execute(
            'INSERT INTO authors(first_name, last_name) VALUES(%s, %s) RETURNING id',
            (first_name, last_name)
        )
        author_id = self.cursor.fetchone()
        self.connection.commit()

        return author_id['id']

    def delete(self, author_id):
        self.cursor.execute('DELETE FROM authors WHERE id=%s', (author_id,))
        self.connection.commit()
