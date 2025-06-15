from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  prompt = None
  if request.method=='POST':
    prompt=request.form['prompt']
  return render_template('home.html', prompt=prompt)
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
