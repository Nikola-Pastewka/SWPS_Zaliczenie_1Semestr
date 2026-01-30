# config.py - Plik konfiguracyjny aplikacji Flask
# Zawiera ustawienia dla różnych środowisk (dev, prod, test)

import os
from datetime import timedelta


class Config:
    # Baza danych
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-WTF (formularze)
    WTF_CSRF_TIME_LIMIT = None  # Brak limitu czasu dla CSRF tokena
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Pagination
    ITEMS_PER_PAGE = 20


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
    # Baza danych - musi być ustawiona w zmiennych środowiskowych
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    # Security
    SESSION_COOKIE_SECURE = True