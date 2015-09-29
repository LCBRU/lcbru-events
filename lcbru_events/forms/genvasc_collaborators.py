from flask_wtf import Form, RecaptchaField, Form
from wtforms import StringField, HiddenField, SelectField, RadioField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField

class PracticeForm(Form):
    practice_code = StringField('Practice Code', validators=[DataRequired(), Length(max=10)])

class AttendeeForm(Form):
    practice_code = HiddenField('practice_code')
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=50)])
    role = SelectField('Role', choices=[('', ''), ('GP', 'GP'), ('Practice Manager', 'Practice Manager'), ('Nurse', 'Nurse'), ('Health Care Assisstant', 'Health Care Assisstant'), ('Phlebotomist', 'Phlebotomists'), ('Administrator', 'Administrator'), ('Other', 'Other')])
    dietary = StringField('Special Dietary Needs', validators=[Length(max=200)])
    meeting = RadioField('Meeting', choices=[('20151202', 'Wednesday, 2nd December 2015'), ('20151208', 'Tuesday, 8th December 2015'), ('other', 'Neither date is convenient, but interested in future dates')])
