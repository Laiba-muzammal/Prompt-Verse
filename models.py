from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'  # recommended
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    prompts = db.relationship('Prompts', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name} - {self.email}>"
class Prompts(db.Model):   
    __tablename__ = 'prompts_history'   

    id = db.Column(db.Integer, primary_key=True)

    prompt_text = db.Column(db.Text, nullable=False)     
    ai_response = db.Column(db.Text, nullable=False)    

    is_favorite = db.Column(db.Boolean, default=False)   
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
