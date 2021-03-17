from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
	movie = StringField('Movie', validators=[DataRequired()])
	review = TextAreaField('Review', validators=[DataRequired()])
	submit = SubmitField('Post')