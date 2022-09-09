## RUN THE APP
from server_folder import db

## SEED DATABASE
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# app = Flask(__name__)
# db = SQLAlchemy()


class Area(db.Model):
    __tablename__ = 'areas'

    area_id = db.Column(db.Integer, primary_key=True)
    biome = db.Column(db.String(255), nullable=False)
    coordinates = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Area: {self.area_id} in {self.biome} at {self.coordinates}"


class Event(db.Model):
    __tablename__ = 'events'

    event_id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(255), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey("areas.area_id"))
    left_coord = db.Column(db.Integer)
    top_coord = db.Column(db.Integer)
    xy = db.Column(db.Integer)
    image = db.Column(db.String(255), nullable=False)
    width = db.Column(db.Integer, default=70) 

    def __repr__(self):
        return f"Event: {self.event} ({self.event_id}) in {self.area_id} at {self.left_coord} / {self.top_coord}"


class Type(db.Model):
    __tablename__ = 'types'

    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    super_effective = db.Column(db.String(255))
    not_effective = db.Column(db.String(255))
    vulnerable_to = db.Column(db.String(255))
    resistant_to = db.Column(db.String(255))


class Dinimon(db.Model):
    __tablename__ = 'dinimon'

    dinimon_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String(255), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    type1 = db.Column(db.Integer, db.ForeignKey("types.type_id"))
    type2 = db.Column(db.Integer, db.ForeignKey("types.type_id"))
    line = db.Column(db.String(255), nullable=False)
    can_evolve = db.Column(db.Boolean)
    rarity = db.Column(db.Integer)
    biomes = db.Column(db.String(255))
    health_range = db.Column(db.String(255), nullable=False)
    energy_range = db.Column(db.String(255), nullable=False)
    possible_moves = db.Column(db.String(255), nullable=False)


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hayde:haz@localhost/dinimon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to DB.")