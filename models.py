import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    wone = db.Column(db.String)
    wtwo = db.Column(db.String)
    wthree = db.Column(db.String)
    wfour = db.Column(db.String)
    wfive = db.Column(db.String)
    wsix = db.Column(db.String)
    um = db.Column(db.String)
