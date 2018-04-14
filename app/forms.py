from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms.validators import InputRequired, DataRequired


class UploadForm (FlaskForm):
    description = TextAreaField('Description', validators = [DataRequired("Description is required")])
    photo = FileField('images', validators=[FileRequired("Please input file"),FileAllowed(['jpg','png','jpeg'], 'Only jpg,jpeg and png images can be uploaded!')])