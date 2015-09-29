import datetime
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('lcbru_events.settings')

db = SQLAlchemy(app)

import lcbru_events.database
database.init_db()

app.secret_key = app.config['SECRET_KEY']

@app.before_request
def set_date():
    g.year = datetime.datetime.now().year

import lcbru_events.helpers.templateFilters

from lcbru_events.views import *