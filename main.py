from flask import Flask, render_template, request, redirect, url_for, SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']=sqlite:///prompts.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

prompts_list=[]

@app.route('/', methods=['GET', 'POST'])
def home():
  prompt = None
  error = None
  if request.method=='POST':
    prompt=request.form['prompt']
    if (not prompt or prompt.strip() ==" "):
      error="Enter a valid input!"
    else:
      prompts_list.append(prompt)
      return redirect(url_for('thanks'))
  return render_template('home.html', prompts=prompts_list, error=error)

@app.route('/prompts')
def prompts():
  return render_template('prompts.html', prompts=prompts_list)

@app.route('/thanks')
def thanks():
  return render_template('thanks.html')


@app.route('/about')
def about():
  return render_template('about.html')

class Prompts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.Text, nullable=False)
  category = db.Column(db.String(100))

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
