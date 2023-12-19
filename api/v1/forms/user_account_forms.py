#!venv/bin/python3
from flask_wtf import FlaskForm
from wtforms import EmailField, IntegerField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    first_name = StringField('First Name',
                             validators=[DataRequired()])
    last_name = StringField('Last Name')
    email = EmailField('Email Address',
                       validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    cohort = IntegerField('Cohort')
    password = PasswordField('Enter Password',
                             validators=[DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField('Repeat Password',
                            validators=[DataRequired(),
                             EqualTo("password", message="Passwords must match.")])
    
    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate(extra_validators)
        if not initial_validation:
            return False
        from models import storage
        from models.user import User
        users = [user for user in storage.all(User).values() if user.email == self.email]
        user = users[0] if users else None
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True
    
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])