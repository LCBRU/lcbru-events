from lcbru_events import db

class Practice(db.Model):
    __tablename__ = 'genvasc_collaborators_practice'

    id = db.Column(db.Integer, primary_key=True)
    practiceCode = db.Column(db.String(20))

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.practiceCode = kwargs.get('practiceCode')

    def delegate_allocation_full(self):
        return (len(self.delegates) >= 2)

class Delegate(db.Model):
    __tablename__ = 'genvasc_collaborators_delegate'

    id = db.Column(db.Integer, primary_key=True)
    practiceId = db.Column(db.Integer, db.ForeignKey('genvasc_collaborators_practice.id'))
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(200))
    role = db.Column(db.String(50))
    dietary = db.Column(db.String(200))
    meetingId = db.Column(db.Integer, db.ForeignKey('genvasc_collaborators_meeting.id'))
    practice = db.relationship("Practice", backref=db.backref('delegates', order_by=id, cascade="all, delete-orphan"))
    meeting = db.relationship("Meeting", backref=db.backref('delegates', order_by=id, cascade="all, delete-orphan"))

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.practiceId = kwargs.get('practiceId')
        self.fullname = kwargs.get('fullname')
        self.email = kwargs.get('email')
        self.role = kwargs.get('role')
        self.dietary = kwargs.get('dietary')
        self.meetingId = kwargs.get('meetingId')

class Meeting(db.Model):
    __tablename__ = 'genvasc_collaborators_meeting'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    spaces = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.spaces = kwargs.get('spaces')

    def full(self):
        return len(self.delegates) >= self.spaces
