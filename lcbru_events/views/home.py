from flask import render_template

from lcbru_events import app

@app.route('/')
def index():
	return render_template('index.html')
