from flask import Flask
from config import basedir
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
