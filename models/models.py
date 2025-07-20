from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    # ... add more fields as needed

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    purchase_date = db.Column(db.Date, nullable=True)
    parts = db.relationship('Part', backref='bike', lazy=True)
    rides = db.relationship('Ride', backref='bike', lazy=True)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    install_date = db.Column(db.Date, nullable=True)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=True)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    distance = db.Column(db.Float, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    map_file = db.Column(db.String(256), nullable=True)  # GPX/KML file path
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=False)

class CalendarEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)  # ride/maintenance
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=True)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=True)
    ride_id = db.Column(db.Integer, db.ForeignKey('ride.id'), nullable=True)

    user = db.relationship('User', backref='events')
    bike = db.relationship('Bike', backref='events')
    part = db.relationship('Part', backref='events')
    ride = db.relationship('Ride', backref='events')
