from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from .models import *

app = Flask(__name__)
#db = SQLAlchemy(app)
#db.init_app(app)

app.config.from_pyfile('config.py')


from app import views, models
