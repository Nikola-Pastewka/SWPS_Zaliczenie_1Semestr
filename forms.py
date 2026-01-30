
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, DateField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, Optional
from wtforms.widgets import DateTimeLocalInput
from models import User
from datetime import datetime


class OptionalDateTimeField(DateField):
    from wtforms import DateField
    from wtforms.validators import Optional

class TaskForm(FlaskForm):
    due_date = DateField('Data wykonania', format='%Y-%m-%d', validators=[Optional()])

    def process_data(self, value):
        if value:
            # Jeśli wartość jest datetime, skonwertuj na string w formacie datetime-local
            self.data = value.strftime('%Y-%m-%dT%H:%M') if isinstance(value, datetime) else value
        else:
            self.data = None

    def process_form_data(self, value):
        if not value or not value[0] or value[0].strip() == '':
            self.data = None
        else:
            try:
                # HTML5 datetime-local wysyła format: YYYY-MM-DDTHH:mm
                self.data = datetime.strptime(value[0], '%Y-%m-%dT%H:%M')
            except (ValueError, IndexError, TypeError) as e:
                # Jeśli format nie pasuje, spróbuj innych formatów lub ustaw None
                self.data = None

# Formularz rejestracji użytkownika
# Zawiera pola na nazwę użytkownika, email, hasło i potwierdzenie hasła oraz przycisk do rejestracji.
# Waliduje unikalność nazwy użytkownika i email oraz zgodność haseł
class RegistrationForm(FlaskForm):
    username = StringField('Nazwa użytkownika',
                          validators=[DataRequired(message='To pole jest wymagane'),
                                    Length(min=3, max=80, message='Nazwa musi mieć od 3 do 80 znaków')])
    email = StringField('Email',
                       validators=[DataRequired(message='To pole jest wymagane'),
                                 Email(message='Podaj poprawny adres email')])
    password = PasswordField('Hasło',
                            validators=[DataRequired(message='To pole jest wymagane'),
                                      Length(min=6, message='Hasło musi mieć co najmniej 6 znaków')])
    password_confirm = PasswordField('Potwierdź hasło',
                                    validators=[DataRequired(message='To pole jest wymagane'),
                                              EqualTo('password', message='Hasła muszą się zgadzać')])
    submit = SubmitField('Zarejestruj się')

    # Sprawdza czy nazwa użytkownika już istnieje w bazie danych.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ta nazwa użytkownika już istnieje. Wybierz inną.')

    # Sprawdza czy email już istnieje w bazie danych.
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Ten email jest już zarejestrowany. Użyj innego.')

# Formularz logowania użytkownika
# Zawiera pola na nazwę użytkownika i hasło oraz przycisk do zalogowania.
# Waliduje obecność obu pól.
class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika',
                          validators=[DataRequired(message='To pole jest wymagane')])
    password = PasswordField('Hasło',
                            validators=[DataRequired(message='To pole jest wymagane')])
    remember = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj się')

# Formularz do dodawania i edycji zadań
# Zawiera pola na tytuł, opis, datę wykonania, pilność i powtarzanie.
# Waliduje długość tytułu i opisu.
class TaskForm(FlaskForm):
    title = StringField('Tytuł zadania',
                       validators=[DataRequired(message='Tytuł nie może być pusty'),
                                 Length(max=200, message='Tytuł nie może być dłuższy niż 200 znaków')])
    description = TextAreaField('Opis (opcjonalne)',
                               validators=[Length(max=1000, message='Opis nie może być dłuższy niż 1000 znaków')])
    category = SelectField('Kategoria (opcjonalne)',
                          choices=[],
                          validators=[Optional()])
    due_date = OptionalDateTimeField('Data wykonania (opcjonalne)',
                                     widget=DateTimeLocalInput(),
                                     validators=[Optional()])
    is_urgent = BooleanField('Oznacz jako pilne')
    repeat_type = SelectField('Powtarzanie',
                             choices=[('', 'Bez powtarzania'),
                                      ('daily', 'Codziennie'),
                                      ('weekly', 'Co tydzień'),
                                      ('monthly', 'Co miesiąc')])
    submit = SubmitField('Zapisz zadanie')

# Formularz do dodawania nowych kategorii
# Zawiera pole na nazwę kategorii oraz przycisk do dodania.
# Waliduje długość nazwy kategorii.
class CategoryForm(FlaskForm):
    name = StringField('Nazwa kategorii',
                      validators=[DataRequired(message='Nazwa kategorii nie może być pusta'),
                                Length(min=1, max=100, message='Nazwa musi mieć od 1 do 100 znaków')])
    submit = SubmitField('Dodaj kategorię')

# Formularz wyszukiwania zadań
# Zawiera pole na zapytanie wyszukiwania oraz przycisk do wyszukania.
# Waliduje długość zapytania wyszukiwania.
class SearchForm(FlaskForm):
    search = StringField('Szukaj',
                        validators=[Length(max=200, message='Zapytanie nie może być dłuższe niż 200 znaków')])
    submit = SubmitField('Szukaj')