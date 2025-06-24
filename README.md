# PromptVerse
# 🌐 Prompt‑Verse

A beginner‑friendly Flask web app where users can submit prompts and get AI‑generated responses via Hugging Face. Includes signup, login, session handling, and a history of all prompts.

---

## 🚀 Features

- 🔐 User Signup, Login, Logout  
- 🧠 AI‑powered responses via Hugging Face API  
- 📚 Prompt history saved per user  
- 🛡️ Secure password hashing & session control  
- 🧩 Modular structure using Flask Blueprints  

---

## 📁 Project Structure

Prompt‑Verse/
├── prompts/ # Flask Blueprint
│ └── routes.py
├── templates/ # Jinja2 templates
│ └── *.html
├── static/
│ └── style.css
├── models.py # Database models
├── create_db.py # Setup DB
├── app.py # Main Flask app runner
├── requirements.txt # Python dependencies
├── .env (ignored) # Config variables
└── README.md

---

## 💻 Setup & Run Locally

git clone https://github.com/Laiba-muzammal/Prompt‑Verse.git
cd Prompt‑Verse

# Virtual environment
python -m venv env
env\Scripts\activate           # Windows
# OR source env/bin/activate   # macOS/Linux

pip install -r requirements.txt

# Create config
echo API_KEY=your_huggingface_key > .env

# Initialize database
python create_db.py

# Run app
python app.py
Visit http://127.0.0.1:5000 to view the app.

📝 Usage
Signup and login

Enter a prompt on the home page

Submit to get an AI response

View your prompt history anytime

👩‍💻 Contributing
PRs welcome! For major changes, please open an issue first.

💬 Author
Laiba Muzammal
GitHub Profile
