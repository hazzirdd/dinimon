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

    def __repr__(self):
        return f"Event: {self.event} ({self.event_id}) in {self.area_id} at {self.left_coord} / {self.top_coord}"

# class Area_Event(db.Model):
#     __tablename__ = 'area_events'

#     area_event_id = db.Column(db.Integer, primary_key=True)
#     area_id = db.Column(db.Integer)
#     event_id = db.Column(db.Integer) 


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hayde:haz@localhost/dinimon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to DB.")