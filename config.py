# -*- encoding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# configuration
DEBUG = True
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/demo.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(__name__)

# database configuration
db = SQLAlchemy()
db.init_app(app)
Migrate(app, db)

@app.before_first_request
def initialize_database():
    db.create_all()

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

# login configuration
login_manager = LoginManager()
login_manager.init_app(app)




