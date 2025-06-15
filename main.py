
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prompts')
def prompts():
    return render_template('prompts.html')

@app.route('/add_prompts', methods=['GET', 'POST'])
def add_prompts():
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render_template('add_prompts.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
