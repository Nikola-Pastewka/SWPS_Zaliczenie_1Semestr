
# Dokumentacja Systemu TaskFlow

## 1. Cel i Przeznaczenie Aplikacji

**TaskFlow** to nowoczesna, responsywna aplikacja webowa typu **To-Do**, zaprojektowana w nurcie minimalistycznego designu.
 Jej głównym celem jest umożliwienie użytkownikom efektywnego zarządzania czasem i obowiązkami poprzez przejrzystą kategoryzację zadań, monitorowanie terminów oraz analizę postępów w czasie rzeczywistym. System został zbudowany z myślą o bezpieczeństwie danych oraz skalowalności kodu.


## 2. Wykorzystane technologie

* Flask
* Flask-Login
* Flask-WTF
* Werkzeug

* SQLAlchemy
* Flask-Migrate
* SQLite/PostgreSQL

* Jinja2
* Bootstrap 5
* Custom CSS
* FontAwesome


## 3. Pełna Lista Możliwości i Funkcjonalności

### A. Zarządzanie Kontem Użytkownika

* Rejestracja: Tworzenie unikalnego konta z walidacją adresu email i siły hasła.
* Logowanie: Bezpieczny dostęp do danych z opcją trwałej sesji.
* Ustawienia Profilu: Zmiana nazwy użytkownika, adresu e-mail oraz hasła bezpośrednio w panelu.
* Usuwanie Konta: Funkcja "Zapomnij o mnie" – kaskadowe usuwanie wszystkich danych użytkownika (zadania, kategorie) przy likwidacji konta.

### B. System Zadań (Task Management)

* Pełny CRUD: Dodawanie, edytowanie, wyświetlanie i usuwanie zadań.
* Interaktywny Status:Możliwość przełączania statusu "Wykonane" oraz "Pilne"
* Zarządzanie Terminami: Obsługa dat i godzin wykonania z widgetem kalendarza HTML5.
* Śledzenie Zaległości: System automatycznie rozpoznaje i może oznaczać zadania, których termin już upłynął.

### C. Kategoryzacja i Organizacja**

* Dynamiczne Kategorie: Użytkownik może tworzyć własne kategorie (np. Praca, Dom, Hobby).
* Kaskadowość: Usuwanie kategorii może automatycznie czyścić powiązane z nią zadania, dbając o porządek w bazie danych.

### D. Widoki i Analiza Danych

* Dashboard: Panel podsumowujący z zaawansowanymi statystykami (liczba zadań ogółem, ukończonych, pozostałych i pilnych).
* Lista Zadań: Tabela z zaawansowanym filtrowaniem i wyszukiwarką pełnotekstową (tytuł/opis).
* Kalendarz: Interaktywny widok miesięczny mapujący zadania na konkretne dni miesiąca.


## 4. Podsumowanie Struktury Bazy Danych

System wykorzystuje trzy powiązane tabele:

1. Users: Przechowuje tożsamość, hashe haseł i datę dołączenia.
2. Categories: Wiąże nazwy z konkretnym użytkownikiem.
3. Tasks: Główna tabela z logiką relacyjną – każde zadanie musi należeć do użytkownika i może (opcjonalnie) należeć do kategorii.
