# lcbru-events

Allow participants to register for events at the LCBRU

## Requirements

    sudo apt-get install libmysqlclient-dev python-dev
    sudo easy_install flask
    sudo easy_install flask-sqlalchemy
    sudo easy_install mysql-python
    sudo pip install Flask-WTF
    sudo pip WTForms-Components

## Install

1. Copy or clone the source from the git repository.
2. Copy the defaultSettings.py file to settings.py
3. Edit the settings.py file and change the following settings:
	1. Change `Debug` to be false
	2. Change `SECRET_KEY` to a secret key.
	3. Change `DATABASE` to the database name
	4. Change `SQLALCHEMY_DATABASE_URI` to a valid MySQL connection string

## Create the database

The lcbru-events application creates the tables that it requires,
but first you must create the database and give the user then
necessary permissions.

1. `CREATE DATABASE lcbru_events;`
2. `GRANT ALL PRIVILEGES ON lcbru_events.* to {username}@127.0.0.1 identified by '{password}';`

## Installation on University of Leicester LAMP servers

See [Here](http://lcbru-trac.rcs.le.ac.uk/wiki/LCBRU%20Events%20Registration%20Website%20HowTo%20Install).