from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from .models import *
from flask_login import LoginManager

app = Flask(__name__)
# db = SQLAlchemy(app)
# db.init_app(app)
lm = LoginManager(app)

# 设置登陆视图的名称
lm.login_view = 'home'
# 当未登录的用户请求一个只有登陆用户才能访问的视图时，闪现错误
lm.login_message = 'Unauthorized User'
# 设置闪现的错误消息的类别
lm.login_message_category = "info"
app.config.from_pyfile('config.py')
lm.anonymous_user = AnonymousUser

from app import views, models
