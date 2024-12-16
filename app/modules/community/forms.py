from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CommunityForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(min=3, max=500)]
    )
    submit = SubmitField("Create Community")


class EditCommunityForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(min=3, max=500)]
    )
    submit = SubmitField("Save changes")
