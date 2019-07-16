from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField
from wtforms.validators import DataRequired,EqualTo

class LoginForm(FlaskForm):
    account=StringField('account',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    remember_me=BooleanField('remember_me',default=False)

class SigninForm(FlaskForm):
    account=StringField('account',validators=[DataRequired()])
                        #,[validators.DataRequired])
    password1=PasswordField('password1',validators=[EqualTo('password1')])
    password2=PasswordField('password2')