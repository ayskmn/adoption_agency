from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, Optional, URL

class AddPetForm(FlaskForm):
	"""Add a new pet."""

	name = StringField("Name", validators=[InputRequired()])
	species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
	photo_url = StringField("Photo URL", validators=[Optional(), URL()])
	age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
	notes = StringField("Notes", validators=[Optional(), Length(min=5)])

class EditPetForm(FlaskForm):
	"""Edit a pet from the database"""

	photo_url = StringField("Photo URL", validators=[Optional(), URL()])
	notes = StringField("Notes", validators=[Optional(), Length(min=5)])
	available = BooleanField("Available:")
