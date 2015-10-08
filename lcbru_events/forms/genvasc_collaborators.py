from flask_wtf import Form, RecaptchaField, Form
from wtforms import StringField, HiddenField, SelectField, RadioField, FormField, Form as WtfForm
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField

class PracticeForm(Form):
    practice_code = StringField('Practice Code', validators=[DataRequired(), Length(max=10)])

class DelegateEditForm(Form):
    id = HiddenField('id')
    fullname = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=200)])
    role = SelectField('Role', choices=[('', ''), ('GP', 'GP'), ('Practice Manager', 'Practice Manager'), ('Nurse', 'Nurse'), ('Health Care Assisstant', 'Health Care Assisstant'), ('Phlebotomist', 'Phlebotomists'), ('Administrator', 'Administrator'), ('Other', 'Other')])
    dietary = StringField('Special Dietary Needs', validators=[Length(max=200)])
    meetingId = RadioField('Meeting', coerce=int)

class DelegateDeleteForm(Form):
    id = HiddenField('id')