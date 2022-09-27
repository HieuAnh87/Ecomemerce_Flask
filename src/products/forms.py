from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, validators, Form
from wtforms.validators import InputRequired


class Addproducts(Form):
    name = StringField('Name', [InputRequired()])
    price = IntegerField('Price', [InputRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [InputRequired()])
    description = TextAreaField('Description', [InputRequired()])
    colors = TextAreaField('Colors', [InputRequired()])

    image_1 = FileField('Image 1',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
