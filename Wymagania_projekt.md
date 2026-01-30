# Wymagania Projektu w Pythonie

## Projekt zaliczeniowy:

Projekt zaliczeniowy powinien być przygotowany w Pythonie w formie notatnika Jupyter Notebook lub pliku python. Projekt powinien być udostępniony na GitHubie (ewentualnie przesłany mailem). Proszę o info gdyby ktoś z Państwa miał pomysł na projekt odstający od poniższego zakresu. Do projektu proszę dołączyć krótki opis – skąd pomysł i czemu wasza aplikacja służy.

Projekt należy przesłać przynajmniej dwa dni przed ostatnimi zajęciami (30 stycznia)

## Przykładowe Projekty Zaliczeniowe

### 1. Aplikacja webowa we Flask
- **System zarządzania zadaniami (To-Do List)**
  - Rejestracja i logowanie użytkowników
  - Dodawanie, edycja, usuwanie zadań
  - Oznaczanie zadań jako ukończone
  - Baza danych SQLite + SQLAlchemy

- **Blog / System artykułów**
  - Panel administracyjny
  - Dodawanie postów z kategoriami
  - System komentarzy
  - Wyszukiwarka artykułów

- **Prosty sklep internetowy**
  - Katalog produktów
  - Koszyk zakupowy (sesje)
  - Formularz zamówienia

### 2. Gra w Pygame
- **Gra typu Snake**
  - Sterowanie wężem (klawiatura)
  - Zbieranie jedzenia i wydłużanie węża
  - Wykrywanie kolizji
  - System punktacji

- **Gra typu Pong / Arkanoid**
  - Fizyka odbijania piłki
  - Sterowanie paletką
  - System poziomów trudności

- **Prosta gra platformowa**
  - Ruch postaci i skakanie
  - Kolizje z platformami
  - Zbieranie przedmiotów

### 3. Analiza danych z Pandas
- **Analiza danych sprzedażowych**
  - Wczytywanie danych z CSV
  - Wizualizacja trendów (matplotlib)
  - Statystyki i raporty

- **Analiza danych pogodowych**
  - Pobieranie danych z API lub pliku
  - Agregacja danych (średnie, min, max)
  - Wykresy temperatur

### 4. Aplikacja konsolowa
- **System biblioteczny**
  - Dodawanie/usuwanie książek
  - Wypożyczanie i zwroty
  - Przechowywanie danych w plikach JSON

- **Quiz / Gra tekstowa**
  - Pytania z różnych kategorii
  - System punktacji
  - Ranking graczy

- **Kalkulator finansowy**
  - Obliczanie rat kredytu
  - Przelicznik walut (z API)
  - Historia obliczeń

### 5. Automatyzacja i skrypty
- **Web scraper**
  - Pobieranie danych ze stron (BeautifulSoup/requests)
  - Zapis do pliku CSV/JSON
  - Analiza zebranych danych

- **Organizator plików**
  - Sortowanie plików według typu/daty
  - Zmiana nazw plików wg wzorca
  - Tworzenie kopii zapasowych

---

## Wymagania projektu

Projekt zaliczeniowy powinien zawierać **co najmniej**:
- Wykorzystanie zmiennych i różnych typów danych
- Struktury danych (listy, słowniki)
- Instrukcje warunkowe i pętle
- Własne funkcje
- Elementy programowania obiektowego (klasy)
- Obsługę wyjątków
- Przynajmniej jeden algorytm (sortowanie lub inny)  (na ocenę bardzo dobrą)
- Połączenie z bazą danych (na ocenę bardzo dobrą)

---

Dodatkowo mogę zadać kilka krótkich pytań z poniższego zakresu: Przed odpowiedzią można zajrzeć do notatek / internetu. 

## 1. Zmienne i Typy Danych

### Wymagania:
- Deklaracja i inicjalizacja zmiennych różnych typów
- Typy podstawowe:
  - `int` - liczby całkowite
  - `float` - liczby zmiennoprzecinkowe
  - `str` - łańcuchy znaków
  - `bool` - wartości logiczne (True/False)
  - `None` - wartość pusta
- Konwersja typów (`int()`, `float()`, `str()`, `bool()`)
- Dynamiczne typowanie w Pythonie

---

## 2. Struktury Danych

### Wymagania:
- **Lista (`list`)** - uporządkowana, mutowalna kolekcja
  - Tworzenie, indeksowanie, slicing
  - Metody: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`

- **Krotka (`tuple`)** - uporządkowana, niemutowalna kolekcja
  - Tworzenie i rozpakowywanie krotek

- **Słownik (`dict`)** - kolekcja par klucz-wartość
  - Tworzenie, dostęp do elementów
  - Metody: `keys()`, `values()`, `items()`, `get()`, `update()`

- **Zbiór (`set`)** - nieuporządkowana kolekcja unikalnych elementów
  - Operacje: unia, przecięcie, różnica

---

## 3. Instrukcje Sterujące

### Wymagania:
- **Instrukcje warunkowe:**
  - `if`, `elif`, `else`
  - Operatory porównania: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Operatory logiczne: `and`, `or`, `not`
  - Operator `in` i `not in`

- **Pętle:**
  - `for` - iteracja po sekwencjach
  - `while` - pętla warunkowa
  - `break` - przerwanie pętli
  - `continue` - przejście do następnej iteracji
  - `else` w pętlach
  - Funkcja `range()`
  - List comprehension (wyrażenia listowe)

---

## 4. Programowanie Obiektowe (OOP)

### Wymagania:
- **Klasy i obiekty:**
  - Definicja klasy (`class`)
  - Konstruktor `__init__()`
  - Parametr `self`
  - Atrybuty instancji i klasy

- **Metody:**
  - Metody instancji
  - Metody klasowe (`@classmethod`)
  - Metody statyczne (`@staticmethod`)

- **Enkapsulacja:**
  - Atrybuty publiczne, chronione (`_`) i prywatne (`__`)
  - Właściwości (`@property`, setter, getter)

- **Dziedziczenie:**
  - Dziedziczenie pojedyncze
  - Funkcja `super()`
  - Nadpisywanie metod

- **Polimorfizm:**
  - Nadpisywanie metod w klasach pochodnych
  - Duck typing

---

## 5. Funkcje

### Wymagania:
- Definicja funkcji (`def`)
- Parametry pozycyjne i nazwane
- Wartości domyślne parametrów
- `*args` i `**kwargs`
- Instrukcja `return`
- Zasięg zmiennych (local, global)
- Funkcje lambda
- Dokumentacja funkcji (docstring)
- **Rekurencja:**
  - Funkcje wywołujące same siebie
  - Warunek bazowy (stopu)
  - Przykłady: silnia, ciąg Fibonacciego, przeszukiwanie drzew

---

## 6. Obsługa Wyjątków

### Wymagania:
- Blok `try`, `except`, `else`, `finally`
- Przechwytywanie konkretnych wyjątków
- Rzucanie wyjątków (`raise`)
- Tworzenie własnych wyjątków

---

## 7. Notacja Big O - Złożoność Obliczeniowa

### Wymagania:
- **Pojęcie złożoności obliczeniowej:**
  - Złożoność czasowa - ile czasu zajmuje algorytm
  - Złożoność pamięciowa - ile pamięci zużywa algorytm
  - Analiza najgorszego, średniego i najlepszego przypadku

- **Popularne złożoności (od najszybszej):**
  - `O(1)` - stała (dostęp do elementu tablicy, operacje na słowniku)
  - `O(log n)` - logarytmiczna (wyszukiwanie binarne)
  - `O(n)` - liniowa (iteracja po liście)
  - `O(n log n)` - liniowo-logarytmiczna (Merge Sort, Quick Sort)
  - `O(n²)` - kwadratowa (zagnieżdżone pętle, Bubble Sort)
  - `O(2^n)` - wykładnicza (rekurencyjne Fibonacci bez memoizacji)
  - `O(n!)` - silnia (permutacje)

- **Analiza algorytmów:**
  - Określanie złożoności na podstawie kodu
  - Porównywanie efektywności algorytmów
  - Wpływ rozmiaru danych na czas wykonania

---

## 8. Algorytmy Sortowania

### Wymagania:
- **Bubble Sort (sortowanie bąbelkowe)**
  - Porównywanie sąsiednich elementów i zamiana miejscami
  - Złożoność czasowa: O(n²)

- **Selection Sort (sortowanie przez wybieranie)**
  - Znajdowanie minimum i wstawianie na początek
  - Złożoność czasowa: O(n²)

- **Insertion Sort (sortowanie przez wstawianie)**
  - Wstawianie elementu w odpowiednie miejsce posortowanej części
  - Złożoność czasowa: O(n²)

- **Merge Sort (sortowanie przez scalanie)**
  - Algorytm "dziel i zwyciężaj"
  - Rekurencyjny podział i scalanie
  - Złożoność czasowa: O(n log n)

---

## 9. Struktury Danych - Stosy i Kolejki

### Wymagania:
- **LIFO (Last In, First Out) - Stos**
  - Implementacja stosu w Pythonie (lista jako stos)
  - Operacje: `push` (dodaj), `pop` (usuń), `peek` (podgląd)
  - Zastosowania: cofanie operacji, parsowanie wyrażeń

- **FIFO (First In, First Out) - Kolejka**
  - Implementacja kolejki (`collections.deque`)
  - Operacje: `enqueue` (dodaj), `dequeue` (usuń)
  - Zastosowania: kolejkowanie zadań, BFS

---

## 10. Flask - Framework Webowy

### Wymagania:
- **Podstawy Flask:**
  - Instalacja (`pip install flask`)
  - Tworzenie aplikacji Flask
  - Routing (`@app.route()`)
  - Metody HTTP: GET, POST, PUT, DELETE

- **Szablony:**
  - Jinja2 - silnik szablonów
  - Renderowanie szablonów (`render_template()`)
  - Przekazywanie zmiennych do szablonów

- **Formularze:**
  - Obsługa danych z formularzy (`request.form`)
  - Walidacja danych

- **Metody HTTP:**
  - `GET` - pobieranie danych
  - `POST` - tworzenie nowych zasobów
  - `PUT` - aktualizacja całego zasobu
  - `PATCH` - częściowa aktualizacja zasobu
  - `DELETE` - usuwanie zasobu

- **Kody odpowiedzi HTTP:**
  - `1xx` - informacyjne
  - `2xx` - sukces:
    - `200 OK` - żądanie zakończone sukcesem
    - `201 Created` - zasób utworzony
    - `204 No Content` - sukces bez zawartości
  - `3xx` - przekierowania:
    - `301 Moved Permanently` - trwałe przekierowanie
    - `302 Found` - tymczasowe przekierowanie
  - `4xx` - błędy klienta:
    - `400 Bad Request` - nieprawidłowe żądanie
    - `401 Unauthorized` - brak autoryzacji
    - `403 Forbidden` - dostęp zabroniony
    - `404 Not Found` - zasób nie znaleziony
    - `405 Method Not Allowed` - metoda niedozwolona
  - `5xx` - błędy serwera:
    - `500 Internal Server Error` - wewnętrzny błąd serwera
    - `502 Bad Gateway` - błąd bramy
    - `503 Service Unavailable` - usługa niedostępna

---

## 11. SQLAlchemy - ORM dla Pythona

### Wymagania:
- **Podstawy SQLAlchemy:**
  - Instalacja (`pip install sqlalchemy`, `pip install flask-sqlalchemy`)
  - Konfiguracja połączenia z bazą danych
  - Tworzenie silnika (`create_engine()`)

- **Modele:**
  - Definiowanie modeli (klas) jako tabel
  - Typy kolumn: `Integer`, `String`, `Boolean`, `DateTime`, `Float`
  - Klucze główne i obce
  - Relacje: `relationship()`, `ForeignKey`

- **Operacje CRUD:**
  - Create: `session.add()`, `session.commit()`
  - Read: `session.query()`, `filter()`, `filter_by()`, `all()`, `first()`
  - Update: modyfikacja atrybutów i `commit()`
  - Delete: `session.delete()`

---

## 12. Pandas - Analiza Danych

### Wymagania:
- **Podstawy Pandas:**
  - Instalacja (`pip install pandas`)
  - Importowanie biblioteki (`import pandas as pd`)

- **Struktury danych:**
  - `Series` - jednowymiarowa tablica z etykietami
  - `DataFrame` - dwuwymiarowa tabela danych
  - Tworzenie z list, słowników, plików CSV/Excel

- **Operacje na DataFrame:**
  - Wybieranie kolumn i wierszy (`df['kolumna']`, `df.loc[]`, `df.iloc[]`)
  - Filtrowanie danych (`df[df['kolumna'] > wartość]`)
  - Sortowanie (`sort_values()`, `sort_index()`)
  - Grupowanie (`groupby()`)

- **Wczytywanie i zapisywanie danych:**
  - `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`
  - `df.to_csv()`, `df.to_excel()`, `df.to_json()`

- **Podstawowe operacje:**
  - `head()`, `tail()` - podgląd danych
  - `info()`, `describe()` - statystyki i informacje
  - `shape`, `columns`, `dtypes` - atrybuty DataFrame
  - Obsługa brakujących danych (`isna()`, `fillna()`, `dropna()`)

---

## 13. Praca z Plikami

### Wymagania:
- Otwieranie plików (`open()`)
- Tryby: odczyt (`r`), zapis (`w`), dopisywanie (`a`)
- Menedżer kontekstu (`with`)
- Metody: `read()`, `readline()`, `readlines()`, `write()`

---

