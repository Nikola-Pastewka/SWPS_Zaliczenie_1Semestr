
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import timedelta
import os

# Parametry: config_name (str) - typ konfiguracji ('development' lub 'production')
def create_app(config_name='development'):
    # Set the template folder to app/templates
    basedir = os.path.abspath(os.path.dirname(__file__))
    template_folder = os.path.join(basedir, 'app', 'templates')
    static_folder = os.path.join(basedir, 'app', 'static')
    
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    
    # Konfiguracja aplikacji
    
    # Konfiguracja dla środowiska deweloperskiego
    if config_name == 'development':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir.replace('/app', ''), 'instance', 'todo_app.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
        app.config['DEBUG'] = True
        # Remember me cookie duration (e.g. 7 days)
        app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
    else:
        # Konfiguracja dla produkcji
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///todo_app.db')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key')
        app.config['DEBUG'] = False
        app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
    
    # Inicjalizacja rozszerzeń
    from models import db
    db.init_app(app)
    
    # Migracje bazy danych
    migrate = Migrate(app, db)
    
    # Login Manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Musisz się zalogować aby uzyskać dostęp do tej strony.'
    login_manager.login_message_category = 'info'
    login_manager.user_loader(load_user)
    
    # Rejestracja blueprintów
    from routes import main_bp, auth_bp, task_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    
    # Kontekst aplikacji do tworzenia tabel
    with app.app_context():
        db.create_all()

    # Zwraca skonfigurowaną aplikację Flask
    return app

# Funkcja ładująca użytkownika dla Flask-Login
from models import User
def load_user(user_id):
    return User.query.get(int(user_id))

# Export db for use in run.py
from models import db