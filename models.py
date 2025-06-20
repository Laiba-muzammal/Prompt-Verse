from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prompts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
