Pierwsza Instalacja i uruchomienie

macOS/Linux

```bash

# Tworzenie wirtualnego środowiska
python3 -m venv venv
source venv/bin/activate

# Instalacja zależności
pip install -r requirements.txt

# Tworzenie folderu bazy danych
mkdir instance

# Uruchomienie aplikacji
python run.py
```

Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
mkdir instance
python run.py
```

Otwórz przeglądarkę:

http://127.0.0.1:5000

Kazda kolejna:
# Pomiń "mkdir instance", gdyz migracje zostaly zaimplementowane, resztę powtórz!
