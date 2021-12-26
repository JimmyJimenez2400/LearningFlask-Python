from datetime import timezone
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))#Notw will hold 10000 char
    date = db.Column(db.DateTime(timezone=True), default=func.now())#Gives time stamp of note
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user_id is int, must pass a valid id to column, (One to many relationship)
    
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')#A list that will store diff notes, access notes a user has made
    
