from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, PasswordField, StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired,Email, length, EqualTo
from flask_wtf.file import FileField,FileAllowed

from hello.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),length(min=2,max=20)])
    email = StringField("Email", validators=[DataRequired(), Email() ])
    password  =  PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField('Signup')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is Already Taken. Please choose otherone')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email is Already Taken. Please choose give other')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email() ])
    password  =  PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),length(min=2,max=20)])
    email = StringField("Email", validators=[DataRequired(), Email() ])
    picture = FileField("Update", validators=[FileAllowed(["jpeg","jpg","png"])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The username is Already Taken. Please choose otherone')
    
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('The email is Already Taken. Please choose give other')


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email() ])
    submit = SubmitField('Request Reset')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("No account with email entered!.Register first")
        
class ResetPasswordForm(FlaskForm):
    password  =  PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField('Reset Password')