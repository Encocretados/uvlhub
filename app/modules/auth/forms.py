
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


class DeveloperSingUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Corporate Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    # Campo desplegable para seleccionar el equipo
    team = SelectField('Team', choices=[
        ('University of Seville', 'University of Seville'),
        ('University of Malaga', 'University of Malaga'),
        ('University of Ulm', 'University of Ulm')
    ], validators=[DataRequired()])
    
    submit = SubmitField('Sign up as Developer')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
