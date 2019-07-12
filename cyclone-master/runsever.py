# coding:utf-8
from flask import request, render_template, flash, url_for, redirect, session, Flask
from flask_cors import *
from sqlalchemy.orm.exc import NoResultFound

from DBManager import *
from entities import *
from utils import *

app=Flask(__name__)
#解决跨域问题
CORS(app,supports_credentials=True)
#解决中文显示问题
app.config['JSON_AS_ASCII']=False
#设置密钥
app.config['SECRET_KEY']='CYCLONE_TEMPEST_TORNADO'

#连接数据库
db_manager=DBManager("mysql+mysqlconnector","47.107.86.216:3306","root","0C45313cea34","timecontrol")
if db_manager is not None:
    print("DB is OK!")

# 创建新用户
@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    p_account = request.values.get("account")
    p_password = request.values.get("password")
    print(p_account,p_password)

    db_session = db_manager.create_session()

    try:
        user_exist = db_session.query(User).filter(User.account == p_account).one()
    except NoResultFound:
        user_exist = None

    if user_exist is None:
        user = User(account=p_account,password=p_password)
        db_session.add(user)
        db_session.commit()
        user_new = db_session.query(User).filter(User.account == p_account).one()
        msg = Message("创建用户成功", 1)
        str_json = user_new.to_json(msg)
    else:
        msg = Message("用户已存在", 2)
        str_json = user_exist.to_json(msg)

    db_session.close()

    return str_json


@app.route('/')
def show_entries():
    db_session = db_manager.create_session()
    categorys = db_session.query(User)
    return render_template('show_entries.html', entries=categorys)


@app.route('/login',methods=['GET','POST'])
def login():
    db_session = db_manager.create_session()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db_session.query(User).filter_by(account=request.form['username']).first()
        passwd = db_session.query(User).filter_by(password=request.form['password']).first()

        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/add',methods=['POST'])
def add_entry():
    db_session = db_manager.create_session()
    if not session.get('logged_in'):
        flash(401)
    title = request.form['title']
    content = request.form['text']
    category = Summary(sum)
    db_session.add(category)
    db_session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


#登出
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(debug=True)
