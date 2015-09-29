import datetime
from lcbru_events import app

@app.template_filter('datetime_format')
def datetime_format(value):
    return value.strftime('%c')
