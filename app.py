from flask import Flask, session, g
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_migrate import Migrate
from prompts.routes import prompts
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate() 
migrate.init_app(app, db) 
app.register_blueprint(prompts)

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    print("Session user_id:", user_id)  
    if user_id is None:
        g.user = None
        print("g.user = None")
    else:
        g.user = User.query.get(user_id)
        print("g.user =", g.user)

if __name__ == "__main__":
    app.run(debug=True)
