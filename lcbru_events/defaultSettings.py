# configuration
DEBUG = True
SECRET_KEY = 'secretkey'

# Database
DATABASE = 'databasename'
SQLALCHEMY_DATABASE_URI = 'connection_string'
SQLALCHEMY_ECHO = True

RECAPTCHA_DATA_ATTRS = {'theme': 'blackglass'}
RECAPTCHA_PUBLIC_KEY = 'Public Key'
RECAPTCHA_PRIVATE_KEY = 'Private Key'

# Emailing
SMTP_SERVER = '127.0.0.1'
ADMIN_EMAIL_ADDRESSES = ['user@example.com']
APPLICATION_EMAIL_ADDRESSES = 'application@example.com'
ERROR_EMAIL_SUBJECT = 'LCBRU Events Failed'
