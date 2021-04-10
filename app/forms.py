from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task = StringField('task', validators=[DataRequired()])
    submit = SubmitField('submit')

class EmptyButton(FlaskForm):
    submit = SubmitField('Submit')