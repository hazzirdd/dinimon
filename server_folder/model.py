## RUN THE APP
from server_folder import db

## SEED DATABASE
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# app = Flask(__name__)
# db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'

    player_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


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
    biome = db.Column(db.String(255), default="Grasslands")
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


class Move(db.Model):
    __tablename__ = 'moves'

    move_id = db.Column(db.Integer, primary_key=True)
    move = db.Column(db.String(255))
    type_id = db.Column(db.Integer, db.ForeignKey("types.type_id"))
    energy_cost = db.Column(db.Integer)
    damage = db.Column(db.String(255))


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
    catchability = db.Column(db.Integer, nullable=False)


class Captured_Dinimon(db.Model):
    __tablename__ = 'captured_dinimon'

    captured_dinimon_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.player_id"))
    dinimon_id = db.Column(db.Integer, db.ForeignKey("dinimon.dinimon_id"))
    nickname = db.Column(db.String(255))
    move1 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    move2 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    move3 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    move4 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    energy = db.Column(db.Integer)
    max_energy = db.Column(db.Integer)
    health = db.Column(db.Integer)
    max_health = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    max_experience = db.Column(db.Integer)
    level = db.Column(db.Integer)
    level_to_evolve = db.Column(db.Integer)
    in_party = db.Column(db.Boolean)
    image = db.Column(db.String(255))


class Enemy_Dinimon(db.Model):
    __tablename__ = 'enemy_dinimon'

    enemy_dinimon_id = db.Column(db.Integer, primary_key=True)
    dinimon_id = db.Column(db.Integer, db.ForeignKey("dinimon.dinimon_id"))
    move1 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    move2 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    move3 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    move4 = db.Column(db.Integer, db.ForeignKey("moves.move_id"))
    type1 = db.Column(db.Integer, db.ForeignKey("types.type_id"))
    type2 = db.Column(db.Integer, db.ForeignKey("types.type_id"))
    energy = db.Column(db.Integer)
    max_energy = db.Column(db.Integer)
    health = db.Column(db.Integer)
    max_health = db.Column(db.Integer)
    level = db.Column(db.Integer)


class Item(db.Model):
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    buy_value = db.Column(db.Integer)
    sell_value = db.Column(db.Integer)
    image = db.Column(db.String(255))
    catch_rate = db.Column(db.Integer)


class Inventory(db.Model):
    __tablename__ = 'inventory'

    inventory_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.player_id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(255))
    buy_value = db.Column(db.Integer)
    sell_value = db.Column(db.Integer)
    image = db.Column(db.String(255))
    catch_rate = db.Column(db.Integer)


class Dinidex(db.Model):
    __tablename__ = 'dinidex'

    dinidex_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.player_id"))
    dinimon_id = db.Column(db.Integer, db.ForeignKey("dinimon.dinimon_id"))



def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hayde:haz@localhost/dinimon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    connect_to_db(app)
    print("Connected to DB.")