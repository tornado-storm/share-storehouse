from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, DateField, RadioField, TimeField,TextAreaField
from wtforms.validators import ValidationError,DataRequired, EqualTo, Required
import datetime


class LoginForm(FlaskForm):
    account = StringField('account', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class SigninForm(FlaskForm):
    account = StringField('account', validators=[DataRequired()])
    # ,[validators.DataRequired])
    password1 = PasswordField('password1', validators=[EqualTo('password1')])
    password2 = PasswordField('password2')

#自定义验证器，验证输入时间是否早于当前时间
def time_check(form,field):
    if field.data<str(datetime.date(datetime.now())):
        raise ValidationError('You can only choose the time inthe future.')

#打印任务的表单，获取时间
class ShowForm(FlaskForm):
    date = DateField('date')

#创建任务的表单
class TaskForm(FlaskForm):
    label = RadioField('label', choices=[
        ('1', '工作'),
        ('2', '生活'),
        ('3', '学习'),
        ('4', '娱乐')
    ], validators=[DataRequired()])
    name = StringField('name')
    level = RadioField('level',choices=[
        ('1','无'),
        ('2','低'),
        ('','中'),
        ('','高')
    ],validators=[DataRequired()])
    date = DateField('date',validators=[DataRequired(),time_check],format='%Y-%m-%d',)
    start_time = TimeField('start_time',validators=[DataRequired()])
    end_time = TimeField('end_time',validators=[DataRequired()])
    alarm = RadioField('alarm',choices=[
        ('1','Yes'),
        ('0','No')
    ],validators=[DataRequired()])

#信的表单，有标题和内容两个
class MailForm(FlaskForm):
    title=StringField('title',validators=[DataRequired()])
    content=TextAreaField('content',validators=[DataRequired()])

