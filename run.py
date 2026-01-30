# run.py - Główny plik uruchamiający aplikację Flask

from Parameters import create_app, db
from models import User, Task, Category

# Tworzenie aplikacji Flask
app = create_app('development')

# Uruchamia serwer Flask na localhost:5000 w trybie debug
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Utwórz wszystkie tabele w bazie danych

    # Uruchom serwer
    app.run(
        host='127.0.0.1',  # Localhost
        port=5000,          # Port
        debug=True          # Tryb debug (hot reload)
    )