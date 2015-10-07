from lcbru_events import db

class Practice(db.Model):
    __tablename__ = 'genvasc_collaborators_practice'

    id = db.Column(db.Integer, primary_key=True)
    practiceCode = db.Column(db.String(20))

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.practiceCode = kwargs.get('practiceCode')

class Delegate(db.Model):
    __tablename__ = 'genvasc_collaborators_delegate'

    id = db.Column(db.Integer, primary_key=True)
    practiceId = db.Column(db.Integer, db.ForeignKey('genvasc_collaborators_practice.id'))
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(200))
    role = db.Column(db.String(50))
    dietary = db.Column(db.String(200))
    meeting = db.Column(db.String(50))
    practice = db.relationship("Practice", backref=db.backref('delegates', order_by=id, cascade="all, delete-orphan"))

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.practiceId = kwargs.get('practiceId')
        self.fullname = kwargs.get('fullname')
        self.email = kwargs.get('email')
        self.role = kwargs.get('role')
        self.dietary = kwargs.get('dietary')
        self.meeting = kwargs.get('meeting')
