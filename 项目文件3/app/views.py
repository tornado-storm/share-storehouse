from flask import render_template, flash, redirect, request, abort, url_for
from app import app, lm
from .forms import *
from .models import *
from .DBManager import *
from flask_login import login_user, current_user, login_required
import datetime

# db_manager=DBManager("mysql+mysqlconnector","47.107.86.216:3306","root","0C45313cea34","timecontrol")
db_manager = DBManager()
if db_manager is not None:
    print("DB is OK!")


def query_user(username):
    db_session = db_manager.create_session()
    user = db_session.query(User).filter(username == User.account).first()
    # print(user)
    db_session.close()
    return user


@lm.user_loader
def load_user(account):
    user = query_user(account)
    if user is not None:
        return user


@app.route('/')
@app.route('/index')
def home():
    query_user('2')
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    form = TaskForm()
    return render_template('create_task.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    db_session = db_manager.create_session()
    form = LoginForm()
    # print(ac, ps)
    # 检测表单的填写
    '''
    if form.validate_on_submit():
        if db_session.query(User).filter(ps == User.account).first is None:
            flash('This account is not exist')
            print('error 1')
            return render_template('login.html', form=form)
        elif ps != db_session.query(User).filter(ac == User.account).first().password:
            flash('Password is wrong')
            print('error 2')
            return render_template('login.html', form=form)
        else:
            print('hello')
            flash('Login requested, remember_me=' + str(form.remember_me.data))
            # return redirect('create_task.html')
            return render_template('create_task.html')
        '''
    if form.validate_on_submit():
        ac = form.account.data
        ps = form.password.data
        user = query_user(ac)
        if user is not None and ps == user.password:
            login_user(user, remember=True)
            # print(current_user)
            return redirect(url_for('create_task'))
    # db_session.close()


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    db_session = db_manager.create_session()
    form = SigninForm()
    ac = form.account.data
    ps1 = form.password1.data
    ps2 = form.password2.data
    print(ac, ps1, ps2)
    # 判断ac是否已经存在
    if form.validate_on_submit():
        print('hello')
        if db_session.query(User).filter(ac == User.account).first() is not None:
            flash('This account already exists.')
            abort(101)
        else:
            user = User(account=ac, password=ps1)
            db_session.add(user)
            db_session.commit()
            flash('Sign up successfully')
            curr_user = User()
            curr_user.id = ac
            login_user(curr_user)
            return render_template('create_task.html')
    # db_session.close()


@app.route('/tc')
def tc():
    return render_template('time_controler.html')


@app.route('/tomato')
def tomato():
    return render_template('tomato.html')


@app.route('/mail')
def mail():
    return render_template('time_controler-post.html')


@app.route('/tce')
def tce():
    return render_template('time_controler-evaluate.html')


@app.route('/create_task')
def create_task():
    form = TaskForm()
    return render_template('create_task.html', form=form)


@app.route('/Registration')
def Registration():
    form = SigninForm()
    return render_template('Registration_interface.html'
                           , form=form
                           )


#打印当天的任务
@app.route('/showmission', methods=['GET', 'POST'])
@login_required
def showmission():
    form = ShowForm()
    date=str(datetime.date.today())
    ac=current_user.user_id
    db_session=db_manager.create_session()
    missions=db_session.query(Mission).filter(date==Mission.date).all()
    print(date)
    print('hello')
    print(missions)
    return render_template('test.html',missions=missions)

   # return


@app.route('/cm', methods=['GET', 'POST'])
@login_required
def cm():
    form = TaskForm()
    ac = current_user.account
    db_session = db_manager.create_session()
    user_id = db_session.query(User).filter(ac == User.account).first().user_id
    label = request.form.get('label')
    name = form.name.data
    level = request.form.get('level')
    date = form.date.data
    start_time = form.start_time.data
    end_time = form.end_time.data
    alarm = form.alarm.data
    print(level, label, name, date, start_time, end_time, alarm)
    mission = Mission(user_id=user_id, start_time=start_time, date=date, stop_time=end_time, name=name, label=label,
                      level=level)
    db_session.add(mission)
    db_session.commit()
    db_session.close()
    return redirect("http://www.baidu.com")


'''
@app.route('/writemail')
def writemail():
    form = MailForm()
    title = form.title.data
    content = form.content.data
    mail = Mail(title=title, content=content)
    db_session = db_manager.create_session()
    db_session.add(mail)
    db_session.commit()
    db_session.close()


@app.route('/mailfrompast')
def mf():
    db_session=db_manager.create_session()
    db_session.query()
    ac=current_user.id
    user=db_session.query(User).filter(ac==User.account)
    user_id=user.user_id
'''
