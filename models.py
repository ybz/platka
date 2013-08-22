from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
app.db = db


class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Notebook %r>' % self.name

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'))
    notebook = db.relationship('Notebook', backref=db.backref('notes', lazy='dynamic'))

    def __init__(self, message, notebook):
        self.message = message
        self.notebook = notebook

    def __repr__(self):
        return '<Note %r>' % self.message


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(20), unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def is_authenticated(self):
        return True
    def is_active(self):
        return self.active
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
