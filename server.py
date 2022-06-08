import sqlalchemy
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime

from flask import Flask, request, jsonify


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQL_TRACK_MODIFICATIONS"] = 0

db = sqlalchemy(app)

# Classes represent tables to the ORM:
# Object relational mapper
# ORM uses models for each table

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")