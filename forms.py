from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    type = RadioField('Type', choices=[('student','Student'),('instructor','Instructor')],validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    type = RadioField('Type', choices=[('student','Student'),('instructor','Instructor')],validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditForm(FlaskForm):
    name = StringField(['Name'])
    lastname = StringField(['Last Name'])
    wsuID = StringField(['WSU ID'])
    phone = StringField(['Phone number'])
    submit = SubmitField('Save')
class AddForm(FlaskForm):
	name = StringField(['Course'])
	submit = SubmitField('Add')