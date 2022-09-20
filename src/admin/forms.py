from wtforms import StringField, PasswordField, Form, validators


class RegistrationForm(Form):
    name = StringField('Name',
                       [validators.InputRequired("Please enter your name")])
    username = StringField('Username',
                           [validators.InputRequired("Please enter your username")])
    email = StringField('Email',
                        [validators.InputRequired("Please fill your email address"),
                         validators.Email("Please enter your email!")])
    password = PasswordField('Password',
                             [validators.InputRequired(),
                              validators.EqualTo('confirm_password', message="Password not match!")])
    confirm_password = PasswordField('Confirm Password',
                                     [validators.InputRequired()])
