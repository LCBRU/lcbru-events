from flask import render_template, redirect, url_for, session, request, flash
from lcbru_events import app
from lcbru_events.forms.genvasc_collaborators import PracticeForm, PracticeDelegatesForm
from lcbru_events.model.genvasc_collaborators import Practice
import time

@app.route('/genvasc_collaborators/', methods=['GET', 'POST'])
def genvasc_collaborators_introduction():
    session['practice_code'] = ''

    form = PracticeForm()

    if form.validate_on_submit():

        practice = Practice.query.filter_by(practiceCode=form.practice_code.data).first()

        if practice:
            session['practice_code'] = form.practice_code.data
            return redirect(url_for('genvasc_collaborators_delegates'))
        else:
            flash("Practice not found", "error")

    if request.method == 'POST':
        time.sleep(5.5)

    return render_template('genvasc_collaborators/introduction.html', form=form)

@app.route('/genvasc_collaborators/delegates/', methods=['GET', 'POST'])
def genvasc_collaborators_delegates():
    if (session['practice_code'] == ''):
        return redirect(url_for('genvasc_collaborators_introduction'))

    form = PracticeDelegatesForm(practice_code = session['practice_code'])

    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('genvasc_collaborators/delegates.html', form=form)
