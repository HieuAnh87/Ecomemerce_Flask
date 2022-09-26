from wtforms import StringField, PasswordField, Form, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class RegistrationForm(Form):
    name = StringField('Name',
                       [InputRequired("Please enter your name")])
    username = StringField('Username',
                           [InputRequired("Please enter your username")])
    email = StringField('Email',
                        [InputRequired("Please fill your email address"),
                         Email("Please enter your email!")])
    password = PasswordField('Password',
                             [InputRequired(),
                              EqualTo('confirm_password', message="Password not match!")])
    confirm_password = PasswordField('Confirm Password',
                                     [InputRequired()])


class LoginForm(Form):
    email = StringField('Email',
                        [InputRequired("Please fill your email address"),
                         Email("Please enter your email!")])
    password = PasswordField('Password', [InputRequired()])
