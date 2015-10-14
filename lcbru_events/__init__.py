import datetime
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('lcbru_events.settings')

db = SQLAlchemy(app)

import lcbru_events.database
database.init_db()

app.secret_key = app.config['SECRET_KEY']

RECAPTCHA_PUBLIC_KEY = app.config['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = app.config['RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}

@app.before_request
def set_date():
    g.year = datetime.datetime.now().year

import lcbru_events.helpers.templateFilters

from lcbru_events.views import *
