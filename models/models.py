from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username: str, password_hash: str, is_admin: bool = False):
        self.username = username
        self.password_hash = password_hash
        self.is_admin = is_admin

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    purchase_date = db.Column(db.Date, nullable=True)

    parts = db.relationship('Part', backref='bike', lazy=True)
    rides = db.relationship('Ride', backref='bike', lazy=True)

    def __init__(self, name: str, brand: str, type: str, purchase_date=None):
        self.name = name
        self.brand = brand
        self.type = type
        self.purchase_date = purchase_date

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    install_date = db.Column(db.Date, nullable=True)

    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=True)

    def __init__(self, name: str, type: str, install_date=None, bike_id=None):
        self.name = name
        self.type = type
        self.install_date = install_date
        self.bike_id = bike_id

class Ride(db.Model):
    def __init__(self, date, distance=None, notes=None, map_file=None, bike_id=None):
        self.date = date
        self.distance = distance
        self.notes = notes
        self.map_file = map_file
        self.bike_id = bike_id
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    distance = db.Column(db.Float, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    map_file = db.Column(db.String(256), nullable=True)  # GPX/KML file path
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=False)

class CalendarEvent(db.Model):

    def __init__(self, title: str, event_type: str, date, notes=None, user_id=None, bike_id=None, part_id=None, ride_id=None, recurrence=None, timezone=None, public=False):
        self.title = title
        self.event_type = event_type
        self.date = date
        self.notes = notes
        self.user_id = user_id
        self.bike_id = bike_id
        self.part_id = part_id
        self.ride_id = ride_id
        self.recurrence = recurrence
        self.timezone = timezone
        self.public = public

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)  # ride/maintenance/race
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bike_id = db.Column(db.Integer, db.ForeignKey('bike.id'), nullable=True)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=True)
    ride_id = db.Column(db.Integer, db.ForeignKey('ride.id'), nullable=True)
    recurrence = db.Column(db.String(64), nullable=True)  # e.g. 'daily', 'weekly', 'custom:RRULE'
    timezone = db.Column(db.String(64), nullable=True)   # e.g. 'America/New_York'
    public = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref='events')
    bike = db.relationship('Bike', backref='events')
    part = db.relationship('Part', backref='events')
    ride = db.relationship('Ride', backref='events')
