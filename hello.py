from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)



@app.route('/')
def index():
	return render_template('index.html')
	

@app.error_handler(400)
def error():
	return render_template('error.html')	

if(__name__ == '__main__'):
	manager.run()