from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(32))
    model = db.Column(db.String(32))
    year = db.Column(db.Integer)
    vin = db.Column(db.String(17))
    odometer = db.Column(db.Integer, default=0)
    color = db.Column(db.String(16))
    owner_name = db.Column(db.String(64))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))