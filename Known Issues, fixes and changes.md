## Known Issues, fixes and changes

## Index
* Przyciski "Zarejestruj się" i "Zaloguj się" znikają w kolorze tła. (FIXED)
* Zmień "Witaj w to-do list" na "Witaj w Taskflow!" (FIXED)
* Zmień Przyciski "Zarejestruj się" i "Zaloguj się" na ponizej "Organizuj swoją pracę, nie przegap żadnego terminu i bądź produktywny!" (FIXED)
* Zmień by było razem: "Aplikacja do zarządzania Twoimi zadaniami i projektami" i "Organizuj swoją pracę, nie przegap żadnego terminu i bądź produktywny!" (FIXED)

## Register Page
* Usuń animację poruszania się formularza po najechaniu. (FIXED)

## Login Page
* Usuń animację poruszania się formularza gdy się najeżdża kursorem. (FIXED)

## Header:
* Header jest przezroczysty i nie jest czytelny. (FIXED)
* Klikanie na konto nic nie powoduje. (FIXED)
* Rozwinięcie konta nie działa na Dashboardzie. (FIXED)
* Dodaj stały separator od headera. (FIXED)

## Sidebar:
* Przestawienie wszystkich rzeczy z headera do sidebara. (FIXED)
* Pierwsza linijka po rozwinięciu jest pusta. (FIXED)
* Usuń Kategorię „Powiadomienia". (FIXED)
* Kategoria „Kalendarz" prowadzi do listy zadań, a nie do jej strony. (FIXED)
* Usuń Kategorię „Karty". (FIXED)
* Usuń "Menu" (FIXED)
* Zmień kolor tekstu z niebieskiego na biały. (FIXED)
* Urywa się. (FIXED)

## Footer:
* Tekst jest zasłonięty przez sidebar. (FIXED)
* Design nie pasuje do interfejsu. (FIXED)
* Dodać autora, link do githuba autora (FIXED)
* Dodać link do githuba projektu (FIXED)
* Skróć długość Footera. (FIXED)
* Dodaj seperator. (FIXED)

## Dashboard:
* Usuń Listę z taskami. (FIXED)
* Usuń gradient na blokach "Razem Zadań", "Ukończone", "Do Zrobienia", "Pilne". (FIXED)
* Zmień nazwę "Panel" na "Główna". (FIXED)
* Usuń kolor czerwony z tekstu "Priorytet wysoki" (FIXED)
* Usuń "Szybkie akcje" i "Informacje" (FIXED)
* Przywitaj nazwę użytkownika. (FIXED)

## Kategorie
* Dodaj opcję wyświetlania obecnych kategorii (FIXED)
* Dodaj opcję edycji kategorii (potwierdzenie) (FIXED)
* Dodaj opcję usunięcia kategorii (potwierdzenie) (FIXED)
* Zmień "Nazwa Kategorii" w Wymienionych obecnych Kategoriach na "Nazwa" i usuń icon. (FIXED)
* Zmień  Kategorię "Akcje" na 2: "Edycja" i "Usuń" (FIXED)
* Dodaj box dla "Twoje kategorie". (FIXED)
* Dodaj box "Dodaj nową kategorię" (FIXED)

## Dodawanie zadania
* Po dodaniu, uzytkownik jest sprowadzony do dashboard, nie do listy. (FIXED)
* Po anulowaniu edycji, uytkownik jest sprowadzony do dashboard, a nie do poprzedniej obecnej strony. (FIXED)
* Data w tworzeniu/edycji zadania wyświetla błąd: Not a valid datetime value. (FIXED)
* Dodaj opcję zaznaczenia kategorii. (FIXED)

## Lista
* Kategorię "Pilne na pierwszym planie" zmienić na "Pilne". (FIXED)
* Dodaj filtrację (FIXED)
* Po kliknięciu "Edit": AttributeError: 'TaskForm' object has no attribute 'category' (FIXED)
* Usunięcie taska przenosi na dashboard. (FIXED)
* Dodaj okno z potwierdzeniem, gdy wybrana jest opcja usunięcia taska. (FIXED)

## Kalendarz
* Wyrzuca błąd: jinja2.exceptions.UndefinedError: 'now' is undefined (FIXED)
* Błąd: TypeError: 'datetime.datetime' object is not callable (FIXED)

## Ustawienia:
* Usuń opcję "Schemat koloru" całkowicie. (FIXED)
* Usuń button "Wróć" (FIXED)

## Wyloguj
* Działa poprawnie. 

## Inne:
* Dodanie icon do preview na górze przegladarki. (FIXED)
* Dodano migrację (FIXED)
* Zmień cały kolor intefejsu by był dark theme z kazdym akcentem kolorystycznym w innych odcieniach szarości. (FIXED)
* ImportError: cannot import name 'create_app' from 'app' (unknown location) (FIXED)
* Error:  Not Found, The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again. (FIXED)
* Error: werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'task.settings'. (FIXED)
* Error: werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'main.index'. (FIXED)


