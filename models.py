from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prompts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(200), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return f"<User {self.name} - {self.email}>"

