from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from ..models.models import User,Contact_us

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender=SelectField('Gender',choices=[('male','Male'),('female','Female')],validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),
                                                             EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ContactUs(FlaskForm):
    name=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    comment=StringField('Comment',validators=[DataRequired()],widget=TextArea())
    submit=SubmitField('Submit')
