from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prompts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(200), unique=True, nullable=False)
    passsword=db.Column(db.String(200), nullable=False)
