from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Prompts
from prompts.routes import prompts

app = Flask(__name__)

app.config['SECRET_KEY'] = 'The Millionaire Laiba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(prompts)

if __name__ == "__main__":
    app.run(debug=True)
