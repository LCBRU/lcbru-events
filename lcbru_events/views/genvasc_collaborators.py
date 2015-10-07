from flask import render_template, redirect, url_for, session, request, flash
from lcbru_events import app, db
from lcbru_events.forms.genvasc_collaborators import PracticeForm, DelegateEditForm
from lcbru_events.model.genvasc_collaborators import Practice, Delegate
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
    practice = Practice.query.filter_by(practiceCode=session['practice_code']).first()

    if (not practice):
        return redirect(url_for('genvasc_collaborators_introduction'))

    return render_template('genvasc_collaborators/delegates.html')

@app.route('/genvasc_collaborators/delegates/new', methods=['GET', 'POST'])
def genvasc_collaborators_delegate_new():
    practice = Practice.query.filter_by(practiceCode=session['practice_code']).first()

    if (not practice):
        return redirect(url_for('genvasc_collaborators_introduction'))

    form = DelegateEditForm()

    if form.validate_on_submit():

        delegate = Delegate(
            practiceId = practice.id,
            fullname = form.fullname.data,
            email = form.email.data,
            role = form.role.data,
            dietary = form.dietary.data,
            meeting = form.meeting.id
            )

        db.session.add(delegate)
        db.session.commit()

        return redirect(url_for('genvasc_collaborators_delegates'))

    return render_template('genvasc_collaborators/delegates_new.html', form=form)
