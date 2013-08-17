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
