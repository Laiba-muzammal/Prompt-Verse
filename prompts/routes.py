from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from models import Prompts, db, User
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv
import os, re, requests

load_dotenv()

prompts = Blueprint("prompts", __name__, template_folder="templates", static_folder="static")

# ------------------------- Custom login_required -------------------------
def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("You must be logged in to access this page.")
            return redirect(url_for('prompts.login'))
        return view(**kwargs)
    return wrapped_view


# ------------------------- HOME -------------------------
@prompts.route('/home', methods=['GET', 'POST'])
@login_required  
def home():
    error = None
    answer = None

    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if not prompt or prompt.strip() == "":
            error = "Enter a valid input!"
        else:
            new_prompt = Prompts(text=prompt, user_id=g.user.id)
            db.session.add(new_prompt)
            db.session.commit()

            # API Call
            headers = {
                "Authorization": f"Bearer {os.getenv('API_KEY')}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": os.getenv('API_MODEL', 'mistralai/mixtral-8x7b-instruct'),
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }

            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    answer = result["choices"][0]["message"]["content"]
                else:
                    error = f"API Error: {response.status_code} - {response.text}"
            except Exception as e:
                error = str(e)

    return render_template('home.html', error=error, answer=answer)


# ------------------------- PROMPTS PAGE -------------------------
@prompts.route('/prompts')
@login_required
def show_prompts():
    all_prompts = Prompts.query.filter_by(user_id=g.user.id).all()
    return render_template('prompts.html', prompts=all_prompts)


# ------------------------- HISTORY PAGE -------------------------
@prompts.route('/history')
@login_required
def history():
    user_prompts = Prompts.query.filter_by(user_id=g.user.id).order_by(Prompts.created_at.desc()).all()
    return render_template('history.html', prompts=user_prompts)


# ------------------------- THANKS PAGE -------------------------
@prompts.route('/thanks')
@login_required
def thanks():
    return render_template('thanks.html')


# ------------------------- ABOUT PAGE -------------------------
@prompts.route('/about')
@login_required
def about():
    return render_template('about.html')


# ------------------------- LANDING -------------------------
@prompts.route('/')
def landing():
    return render_template('index.html')


# ------------------------- LOGIN -------------------------
@prompts.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        if not email or not password:
            flash("Email and password required.")
            return render_template('login.html', email=email)

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash("Login successful!")
            return redirect(url_for('prompts.home'))
        else:
            flash("Invalid email or password.")
            return render_template('login.html', email=email)

    return render_template('login.html')


# ------------------------- SIGNUP -------------------------
@prompts.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not name or not email or not password or not confirm:
            flash("All fields are required!")
            return render_template('signup.html', name=name, email=email)

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format!")
            return render_template('signup.html', name=name, email=email)
        
        if (len(password) < 6 or
            not re.search(r"[A-Za-z]", password) or         
            not re.search(r"\d", password) or               
            not re.search(r"[@$%#&*^_|\\/]", password) ):
            flash("Password must be at least 6 characters long having \n\n • At least one letter (A–Z or a–z)\n\n• At least one number (0–9)\n\n• At least one special character (@$%#&*^_|\\/)")
            return render_template('signup.html', name=name, email=email, password=password)

        if password != confirm:
            flash("Passwords do not match!")
            return render_template('signup.html', name=name, email=email)

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered.")
            return render_template('signup.html', name=name, email=email)

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful! Login now.")
        return redirect(url_for('prompts.login'))

    return render_template('signup.html')


# ------------------------- LOGOUT -------------------------
@prompts.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('prompts.landing'))

