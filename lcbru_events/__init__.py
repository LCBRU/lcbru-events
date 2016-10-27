import datetime
from flask import Flask, g, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import logging
import traceback

app = Flask(__name__)
app.config.from_object('lcbru_events.settings')
app.secret_key = app.config['SECRET_KEY']

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(app.config['SMTP_SERVER'],
                               app.config['APPLICATION_EMAIL_ADDRESSES'],
                               app.config['ADMIN_EMAIL_ADDRESSES'],
                               app.config['ERROR_EMAIL_SUBJECT'])
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

@app.errorhandler(500)
@app.errorhandler(Exception)
def internal_error(exception):
    print(traceback.format_exc())
    app.logger.error(traceback.format_exc())
    return render_template('500.html'), 500

db = SQLAlchemy(app)

import lcbru_events.database
database.init_db()

@app.before_request
def set_date():
    g.year = datetime.datetime.now().year

import lcbru_events.helpers.templateFilters

from lcbru_events.views import *
