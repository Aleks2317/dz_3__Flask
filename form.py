from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Введите ваше имя:', validators=[DataRequired()])
    surname = StringField('Введите вашу фамилию:', validators=[DataRequired()])
    email = EmailField('Введите ваш email:', validators=[DataRequired(), Email()])
    password = PasswordField('Введите ваш пароль:', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Подтвердите ваш пароль:', validators=[DataRequired(), EqualTo('password')])
