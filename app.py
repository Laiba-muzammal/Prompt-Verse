from flask import Flask, session, g
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from prompts.routes import prompts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'The Millionaire Laiba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
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
