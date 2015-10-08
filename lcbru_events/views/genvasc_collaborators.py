from flask import render_template, redirect, url_for, session, request, flash
from lcbru_events import app, db
from lcbru_events.forms.genvasc_collaborators import PracticeForm, DelegateEditForm, DelegateDeleteForm
from lcbru_events.model.genvasc_collaborators import Practice, Delegate, Meeting
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
    practice = _genvasc_collaborator_get_session_practice()

    if (not practice):
        return redirect(url_for('genvasc_collaborators_introduction'))

    return render_template('genvasc_collaborators/delegates.html', practice=practice)

@app.route('/genvasc_collaborators/delegates/new', methods=['GET', 'POST'])
def genvasc_collaborators_delegate_new():
    practice = _genvasc_collaborator_get_session_practice()

    if (not practice):
        return redirect(url_for('genvasc_collaborators_introduction'))

    if (practice.delegate_allocation_full()):
        flash("Cannot add delegate to practice as you have reached your allocation limit.", "error")
        return redirect(url_for('genvasc_collaborators_delegates'))

    form = DelegateEditForm()

    meetings = Meeting.query.all()

    form.meetingId.choices = [(m.id, m.name) for m in meetings if not m.full()]

    print "Meetings: ", form.meetingId.choices;

    if form.validate_on_submit():
        delegate = Delegate(practiceId=practice.id)
        form.populate_obj(delegate)
        db.session.add(delegate)
        db.session.commit()

        return redirect(url_for('genvasc_collaborators_delegates'))

    return render_template('genvasc_collaborators/delegates_new.html', form=form)

@app.route("/genvasc_collaborators/delegates/edit/<int:id>", methods=['GET','POST'])
def genvasc_collaborators_delegate_edit(id):
    practice = _genvasc_collaborator_get_session_practice()
    delegate = Delegate.query.get(id)

    if (practice != delegate.practice):
        flash("Permission denied.", "error")
        return redirect(url_for('genvasc_collaborators_delegates'))        

    form = DelegateEditForm(obj=delegate)

    if form.validate_on_submit():
        form.populate_obj(delegate)
        db.session.add(delegate)
        db.session.commit()
        return redirect(url_for('genvasc_collaborators_delegates'))

    return render_template('genvasc_collaborators/delegates_new.html', form=form)

@app.route("/genvasc_collaborators/delegates/delete/<int:id>")
def genvasc_collaborators_delegate_delete(id):
    delegate = Delegate.query.get(id)
    form = DelegateDeleteForm(obj=delegate)
    return render_template('genvasc_collaborators/delegates_delete.html', delegate=delegate, form=form)

@app.route("/genvasc_collaborators/delegates/delete", methods=['POST'])
def genvasc_collaborators_delegate_delete_confirm():
    form = DelegateDeleteForm()

    if form.validate_on_submit():
        delegate = Delegate.query.get(form.id.data)

        if (delegate):
            db.session.delete(delegate)
            db.session.commit()
            flash("Deleted delegate '%s'." % delegate.fullname)
            
    return redirect(url_for('genvasc_collaborators_delegates'))

def _genvasc_collaborator_get_session_practice():
    return Practice.query.filter_by(practiceCode=session['practice_code']).first()
