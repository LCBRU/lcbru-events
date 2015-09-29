from flask import render_template, redirect, url_for, session
from lcbru_events import app
from lcbru_events.forms.genvasc_collaborators import PracticeForm, AttendeeForm

@app.route('/genvasc_collaborators/', methods=['GET', 'POST'])
def genvasc_collaborators_introduction():
    form = PracticeForm()

    if form.validate_on_submit():
        session['practice_code'] = form.practice_code.data
        return redirect(url_for('genvasc_collaborators_attendees'))

    return render_template('genvasc_collaborators/introduction.html', form=form)

@app.route('/genvasc_collaborators/attendees/', methods=['GET', 'POST'])
def genvasc_collaborators_attendees():
    form = AttendeeForm(practice_code = session['practice_code'])

    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('genvasc_collaborators/attendees.html', form=form)
