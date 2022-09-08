from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath

app.config['SECRET_KEY'] = 'secerets'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hayde:haz@localhost/dinimon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)