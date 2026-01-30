
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Inicjalizacja bazy danych
db = SQLAlchemy()

# Modele bazy danych
# Model użytkownika
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacja z zadaniami
    tasks = db.relationship('Task', backref='user', lazy=True, cascade='all, delete-orphan')
    # Relacja z kategoriami
    categories = db.relationship('Category', backref='user', lazy=True, cascade='all, delete-orphan')

    # Hashuje i zapisuje hasło użytkownika.
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Sprawdza czy podane hasło odpowiada zapisanemu hashowi.
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Zwraca statystyki zadań użytkownika.
    def get_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.is_completed)
        remaining_tasks = total_tasks - completed_tasks
        urgent_tasks = sum(1 for task in self.tasks if task.is_urgent and not task.is_completed)

        return {
            'total': total_tasks,
            'completed': completed_tasks,
            'remaining': remaining_tasks,
            'urgent': urgent_tasks
        }

# Model kategorii zadań
# Każda kategoria należy do konkretnego użytkownika i może mieć wiele zadań.
# Zawiera nazwę, kolor i datę utworzenia.
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(7), default='#3498db')  # Kolor hex dla kategorii
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacja z zadaniami
    tasks = db.relationship('Task', backref='category', lazy=True)

    # Reprezentacja tekstowa obiektu Category
    def __repr__(self):
        return f'<Category {self.name}>'

# Model zadania
# Zawiera tytuł, opis, datę wykonania, status, pilność, powtarzanie oraz klucze obce do użytkownika i kategorii.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  # Max 200 znaków
    description = db.Column(db.String(1000), default='')  # Max 1000 znaków
    due_date = db.Column(db.DateTime)  # Data realizacji
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Status zadania
    is_completed = db.Column(db.Boolean, default=False)
    is_urgent = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='Do zrobienia')  # 'Do zrobienia', 'W trakcie', 'Wykonane', 'Archiwum'

    # Powtarzanie zadania (None, 'daily', 'weekly', 'monthly')
    repeat_type = db.Column(db.String(20), default=None)

    # Klucze obce
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    # Reprezentacja tekstowa obiektu Task
    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'

    # Oblicza ile dni pozostało zadaniu do terminu wykonania.
    def get_days_until_due(self):
        if not self.due_date:
            return None
        delta = self.due_date - datetime.utcnow()
        return delta.days

    # Sprawdza czy zadanie jest zaległe (termin przekroczony).
    def is_overdue(self):
        if not self.due_date or self.is_completed:
            return False
        return datetime.utcnow() > self.due_date

    # Zmienia status ukończenia zadania.
    def toggle_completed(self):
        self.is_completed = not self.is_completed
        self.updated_at = datetime.utcnow()

    # Zmienia status pilności zadania.
    def toggle_urgent(self):
        self.is_urgent = not self.is_urgent
        self.updated_at = datetime.utcnow()