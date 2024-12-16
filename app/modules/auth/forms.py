from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, Length, Optional, Regexp


class SignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    surname = StringField("Surname", validators=[DataRequired(), Length(max=100)])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=20),  # Password length between 8 and 20 characters
            Regexp(r"^(?=.*[A-Z])", message="Password must contain at least one uppercase letter\n"),
            Regexp(r"^(?=.*[a-z])", message="Password must contain at least one lowercase letter\n"),
            Regexp(r"^(?=.*\d)", message="Password must contain at least one digit\n"),  # At least one digit
            Regexp(
                r"^(?=.*[!@#$%^&*()_+={}\[\]:;'\"<>,.?/-])",
                message="Password must contain at least one special character: #,@,~,€\n"),  # Special character
        ]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")


class DeveloperSingUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    email = StringField("Corporate Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=20),  # Password length between 8 and 20 characters
            Regexp(r"^(?=.*[A-Z])", message="Password must contain at least one uppercase letter\n"),
            Regexp(r"^(?=.*[a-z])", message="Password must contain at least one lowercase letter\n"),
            Regexp(r"^(?=.*\d)", message="Password must contain at least one digit\n"),  # At least one digit
            Regexp(
                r"^(?=.*[!@#$%^&*()_+={}\[\]:;'\"<>,.?/-])",
                message="Password must contain at least one special character: #,@,~,€\n"),  # Special character
        ]
    )
    # Campo desplegable para seleccionar el equipo
    team = SelectField(
        "Team",
        choices=[
            ("University of Seville", "University of Seville"),
            ("University of Malaga", "University of Malaga"),
            ("University of Ulm", "University of Ulm"),
        ],
        validators=[DataRequired()],
    )
    # Campo para el usuario de GitHub
    github = StringField(
        "GitHub Username",
        validators=[
            Optional(),
            Length(max=50),
            Regexp(r"^[a-zA-Z0-9_-]+$", message="Enter a valid GitHub username"),
        ],
    )
    submit = SubmitField("Sign up as Developer")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class EmailValidationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    key = StringField('Key', validators=[DataRequired()])
    submit = SubmitField('Validate Email')
