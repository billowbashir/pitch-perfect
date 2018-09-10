from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import Pitch,Comment

class PitchForm(FlaskForm):
    category=SelectField('category',
        choices=[('inspiration', 'inspiration'), ('life hacks', 'life hacks'), ('tech', 'tech'), ('funny', 'funny')], validators = [Required()])
    pitch = TextAreaField('pitch',validators=[Required()])
    submit = SubmitField('submit')
class CommentForm(FlaskForm):
    comment=TextAreaField('comment',validators=[Required()])
    submit = SubmitField('submit')
