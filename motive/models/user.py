from ..database.db import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(500))
    password = db.Column(db.String(500))
#     reviews = db.relationship("Reviews")


# class Reviews(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
