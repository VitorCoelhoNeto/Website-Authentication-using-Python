from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    """
    User class, used to store the Users.
    Inherits from the database Model class and UserMixin.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')



class Note(db.Model):
    """
    Note class used to store the user's notes.
     Inherits from the database Model class.
    """
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))