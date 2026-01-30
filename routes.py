
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user, login_user, logout_user
from sqlalchemy import or_
from models import db, User, Task, Category
from forms import RegistrationForm, LoginForm, TaskForm, CategoryForm, SearchForm
from datetime import datetime

# Tworzenie Blueprint dla tras
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
task_bp = Blueprint('task', __name__)


# STRONA GŁÓWNA

#Jeśli użytkownik jest zalogowany, pokazuje jego zadania.
# W przeciwnym razie pokazuje stronę powitalną.
@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('task.dashboard'))
    return render_template('index.html')


# UWIERZYTELNIANIE

# Obsługuje rejestrację nowego użytkownika.
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('task.login'))
    form = RegistrationForm()

    # Rejestracja nowego użytkownika
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        # Hashowanie hasła
        user.set_password(form.password.data)
        
        # Dodawanie do bazy danych
        db.session.add(user)
        db.session.commit()
        
        # Tworzenie domyślnych kategorii dla nowego użytkownika
        default_categories = [
            Category(name='Praca', color='#1e5a96', user_id=user.id),
            Category(name='Nauka', color='#2a7cbd', user_id=user.id),
            Category(name='Hobby', color='#3d9dd7', user_id=user.id),
            Category(name='Inne', color='#5aafde', user_id=user.id)
        ]
        # Dodawanie domyślnych kategorii do bazy danych
        for cat in default_categories:
            db.session.add(cat)
        db.session.commit()

        # Powiadomienie o sukcesie
        flash('Rejestracja udana! Zaloguj się, aby kontynuować.', 'success')
        return redirect(url_for('auth.login'))  
    
    # Wyświetlanie formularza rejestracji
    return render_template('register.html', form=form)

# Obsługuje logowanie użytkownika.
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('task.dashboard'))
    
    form = LoginForm()

    # Wyszukanie użytkownika w bazie danych
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        # Sprawdzenie hasła
        if user and user.check_password(form.password.data):
            # Use "remember me" flag from the form to create a persistent login cookie
            remember = getattr(form, 'remember', None)
            remember_value = remember.data if remember is not None else False
            login_user(user, remember=remember_value)
            flash(f'Zalogowano jako {user.username}!', 'success')
            return redirect(url_for('task.dashboard'))
        else:
            flash('Błędy dane logowania!', 'danger')

    # Wyświetlanie formularza logowania
    return render_template('login.html', form=form)

# Obsługuje wylogowanie użytkownika.
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Wylogowano pomyślnie.', 'info')
    return redirect(url_for('main.index'))


# ZADANIA

@task_bp.route('/dashboard')
@login_required
def dashboard():
    # Pobranie parametrów z URL
    sort = request.args.get('sort', 'recent')
    category_id = request.args.get('category', None, type=int)
    search_query = request.args.get('search', '')
    
    # Pobranie wszystkich zadań użytkownika
    query = Task.query.filter_by(user_id=current_user.id)
    
    # Filtrowanie po kategorii
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    # Wyszukiwanie po tytule i opisie
    if search_query:
        query = query.filter(
            or_(
                Task.title.ilike(f'%{search_query}%'),
                Task.description.ilike(f'%{search_query}%')
            )
        )
    
    tasks = query.all()
    
    # Sortowanie zadań
    if sort == 'date':
        # Sortuj po dacie (najpierw bez daty, potem rosnąco)
        tasks = sorted(tasks, key=lambda x: (x.due_date is None, x.due_date or datetime.utcnow()))
    elif sort == 'urgent':
        # Sortuj po pilności
        tasks = sorted(tasks, key=lambda x: (not x.is_urgent, x.due_date or datetime.utcnow()))
    else:  # recent
        # Sortuj po dacie dodania (najnowsze najpierw)
        tasks = sorted(tasks, key=lambda x: x.created_at, reverse=True)
    
    # Pobranie kategorii dla tego użytkownika
    categories = Category.query.filter_by(user_id=current_user.id).all()
    
    # Obliczenie statystyk
    stats = current_user.get_statistics()
    
    return render_template('dashboard.html', 
                          tasks=tasks,
                          categories=categories,
                          stats=stats,
                          current_sort=sort,
                          current_category=category_id,
                          search_query=search_query)

@task_bp.route('/task/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    # Ustawienie opcji kategorii z kategorii bieżącego użytkownika
    form.category.choices = [(0, 'Bez kategorii')] + [(cat.id, cat.name) for cat in Category.query.filter_by(user_id=current_user.id).all()]
    
    # Tworzenie nowego zadania
    if form.validate_on_submit():
        category_id = None
        if form.category.data and int(form.category.data) != 0:
            category_id = int(form.category.data)
        
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            is_urgent=form.is_urgent.data,
            repeat_type=form.repeat_type.data if form.repeat_type.data else None,
            category_id=category_id,
            user_id=current_user.id
        )
        
        db.session.add(task)
        db.session.commit()
        
        flash(f'Zadanie "{task.title}" zostało dodane!', 'success')
        return redirect(url_for('task.task_list'))
    
    return render_template('add_task.html', form=form)

#Edycja istniejącego zadania
@task_bp.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Sprawdzenie czy zadanie należy do bieżącego użytkownika
    if task.user_id != current_user.id:
        flash('Nie masz dostępu do tego zadania!', 'danger')
        return redirect(url_for('task.dashboard'))
    
    form = TaskForm()
    # Ustawienie opcji kategorii z kategorii bieżącego użytkownika
    form.category.choices = [(0, 'Bez kategorii')] + [(cat.id, cat.name) for cat in Category.query.filter_by(user_id=current_user.id).all()]

    # Aktualizacja danych zadania
    if form.validate_on_submit():
        category_id = None
        if form.category.data and int(form.category.data) != 0:
            category_id = int(form.category.data)
        
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        task.is_urgent = form.is_urgent.data
        task.repeat_type = form.repeat_type.data if form.repeat_type.data else None
        task.category_id = category_id
        task.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        flash(f'Zadanie "{task.title}" zostało zaktualizowane!', 'success')
        return redirect(url_for('task.task_list'))
    
    # Załadowanie danych do formularza
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.due_date.data = task.due_date
        form.is_urgent.data = task.is_urgent
        form.repeat_type.data = task.repeat_type
        form.category.data = str(task.category_id) if task.category_id else '0'
    
    return render_template('edit_task.html', form=form, task=task)

# Duplikowanie zadania
@task_bp.route('/task/<int:task_id>/duplicate', methods=['GET', 'POST'])
@login_required
def duplicate_task(task_id):
    original_task = Task.query.get_or_404(task_id)
    
    # Sprawdzenie czy zadanie należy do bieżącego użytkownika
    if original_task.user_id != current_user.id:
        flash('Nie masz dostępu do tego zadania!', 'danger')
        return redirect(url_for('task.task_list'))
    
    form = TaskForm()
    # Ustawienie opcji kategorii z kategorii bieżącego użytkownika
    form.category.choices = [(0, 'Bez kategorii')] + [(cat.id, cat.name) for cat in Category.query.filter_by(user_id=current_user.id).all()]

    # Tworzenie nowego zadania na podstawie oryginalnego
    if form.validate_on_submit():
        category_id = None
        if form.category.data and int(form.category.data) != 0:
            category_id = int(form.category.data)
        
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            is_urgent=form.is_urgent.data,
            repeat_type=form.repeat_type.data if form.repeat_type.data else None,
            category_id=category_id,
            user_id=current_user.id
        )
        
        db.session.add(new_task)
        db.session.commit()
        
        flash(f'Zadanie "{new_task.title}" zostało zduplikowane!', 'success')
        return redirect(url_for('task.task_list'))
    
    # Załadowanie danych z oryginalnego zadania
    elif request.method == 'GET':
        form.title.data = f"{original_task.title} (kopia)"
        form.description.data = original_task.description
        form.due_date.data = original_task.due_date
        form.is_urgent.data = original_task.is_urgent
        form.repeat_type.data = original_task.repeat_type
        form.category.data = str(original_task.category_id) if original_task.category_id else '0'
    
    return render_template('edit_task.html', form=form, task=None, is_duplicate=True)

# Usuwanie zadania
@task_bp.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Sprawdzenie czy zadanie należy do bieżącego użytkownika
    if task.user_id != current_user.id:
        flash('Nie masz dostępu do tego zadania!', 'danger')
        return redirect(url_for('task.task_list'))
    
    task_title = task.title
    db.session.delete(task)
    db.session.commit()
    
    flash(f'Zadanie "{task_title}" zostało usunięte!', 'success')
    
    # Wróć na stronę, z której pochodzi żądanie
    referrer = request.referrer
    if referrer and 'task_list' in referrer:
        return redirect(url_for('task.task_list'))
    elif referrer and 'dashboard' in referrer:
        return redirect(url_for('task.dashboard'))
    else:
        return redirect(url_for('task.task_list'))

# Zmiana statusu ukończenia zadania
@task_bp.route('/task/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Sprawdzenie czy zadanie należy do bieżącego użytkownika
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    task.toggle_completed()
    db.session.commit()
    
    return jsonify({
        'success': True,
        'is_completed': task.is_completed,
        'stats': current_user.get_statistics()
    })

# Zmiana statusu pilności zadania
@task_bp.route('/task/<int:task_id>/urgent', methods=['POST'])
@login_required
def toggle_task_urgent(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Sprawdzenie czy zadanie należy do bieżącego użytkownika
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    task.toggle_urgent()
    db.session.commit()
    
    return jsonify({
        'success': True,
        'is_urgent': task.is_urgent
    })


# KATEGORIE

@task_bp.route('/category/add', methods=['GET', 'POST'])
@login_required
def add_category():
    """
    Obsługuje dodawanie nowej kategorii i wyświetlanie istniejących.
    GET: wyświetla formularz i listę kategorii
    POST: przetwarza dane i tworzy nową kategorię
    Zwraca: szablon HTML lub redirect
    """
    form = CategoryForm()

    # Tworzenie nowej kategorii
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            user_id=current_user.id
        )
        
        db.session.add(category)
        db.session.commit()
        
        flash(f'Kategoria "{category.name}" została dodana!', 'success')
        return redirect(url_for('task.add_category'))
    
    # Pobranie wszystkich kategorii użytkownika
    categories = Category.query.filter_by(user_id=current_user.id).all()
    
    return render_template('add_category.html', form=form, categories=categories)

# Usuwanie kategorii
@task_bp.route('/category/<int:category_id>/delete', methods=['POST'])
@login_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    
    # Sprawdzenie czy kategoria należy do bieżącego użytkownika
    if category.user_id != current_user.id:
        flash('Nie masz dostępu do tej kategorii!', 'danger')
        return redirect(url_for('task.add_category'))
    
    category_name = category.name
    # Usunięcie zadań w tej kategorii
    tasks = Task.query.filter_by(category_id=category_id).all()
    for task in tasks:
        db.session.delete(task)
    
    db.session.delete(category)
    db.session.commit()
    
    flash(f'Kategoria "{category_name}" i wszystkie zadania w niej zostały usunięte!', 'success')
    return redirect(url_for('task.add_category'))

# Edycja kategorii
@task_bp.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    
    # Sprawdzenie czy kategoria należy do bieżącego użytkownika
    if category.user_id != current_user.id:
        flash('Nie masz dostępu do tej kategorii!', 'danger')
        return redirect(url_for('task.add_category'))
    
    form = CategoryForm()
    
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash(f'Kategoria "{category.name}" została zaktualizowana!', 'success')
        return redirect(url_for('task.add_category'))
    elif request.method == 'GET':
        form.name.data = category.name
    
    return render_template('edit_category.html', form=form, category=category)

# USTAWIENIA

@task_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """
    Obsługuje stronę ustawień użytkownika.
    Umożliwia zmianę hasła, emaila, nazwy użytkownika i schematu kolorów.
    """
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_email = request.form.get('email')
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        color_scheme = request.form.get('color_scheme', 'blue')
        
        errors = []
        
        # Walidacja nazwy użytkownika
        if new_username and new_username != current_user.username:
            if User.query.filter_by(username=new_username).first():
                errors.append('Nazwa użytkownika już istnieje!')
            else:
                current_user.username = new_username
        
        # Walidacja emaila
        if new_email and new_email != current_user.email:
            if User.query.filter_by(email=new_email).first():
                errors.append('Email już istnieje!')
            else:
                current_user.email = new_email
        
        # Walidacja hasła
        if new_password:
            if new_password != confirm_password:
                errors.append('Hasła nie pasują do siebie!')
            elif len(new_password) < 6:
                errors.append('Hasło musi mieć co najmniej 6 znaków!')
            else:
                current_user.set_password(new_password)
        
        # Zapisanie zmian
        if not errors:
            db.session.commit()
            flash('Ustawienia zostały zaktualizowane!', 'success')
            return redirect(url_for('task.settings'))
        else:
            for error in errors:
                flash(error, 'danger')
    
    return render_template('settings.html', current_user=current_user)

# Usuwanie konta użytkownika
@task_bp.route('/delete-account', methods=['POST'])
@login_required
def delete_account():
    """
    Obsługuje usuwanie konta użytkownika wraz ze wszystkimi jego danymi.
    """
    user_id = current_user.id
    username = current_user.username
    
    # Wyloguj użytkownika
    logout_user()
    
    # Usuń użytkownika i wszystkie jego dane
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash(f'Konto użytkownika "{username}" oraz wszystkie powiązane dane zostały usunięte.', 'info')
    
    return redirect(url_for('main.index'))


# Endpoint dla zmiany schematu kolorów
@task_bp.route('/settings/color-scheme', methods=['POST'])
@login_required
def change_color_scheme():
    data = request.get_json()
    color_scheme = data.get('color_scheme', 'blue')
    
    # Tutaj można zapisać schemat kolorów w bazie danych
    # current_user.color_scheme = color_scheme
    # db.session.commit()
    
    return jsonify({'success': True, 'color_scheme': color_scheme})

# LISTA ZADAŃ

@task_bp.route('/tasks/list')
@login_required
def task_list():
    # Pobranie parametrów z URL
    sort = request.args.get('sort', 'recent')
    category_id = request.args.get('category', None, type=int)
    search_query = request.args.get('search', '')
    status_filter = request.args.get('status', '')
    
    # Pobranie wszystkich zadań użytkownika
    query = Task.query.filter_by(user_id=current_user.id)
    
    # Filtrowanie po kategorii
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    # Filtrowanie po statusie
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    # Wyszukiwanie po tytule i opisie
    if search_query:
        query = query.filter(
            or_(
                Task.title.ilike(f'%{search_query}%'),
                Task.description.ilike(f'%{search_query}%')
            )
        )
    
    tasks = query.all()
    
    # Sortowanie zadań
    if sort == 'date':
        tasks = sorted(tasks, key=lambda x: (x.due_date is None, x.due_date or datetime.utcnow()))
    elif sort == 'urgent':
        tasks = sorted(tasks, key=lambda x: (not x.is_urgent, x.due_date or datetime.utcnow()))
    else:  # recent
        tasks = sorted(tasks, key=lambda x: x.created_at, reverse=True)
    
    # Pobranie kategorii dla tego użytkownika
    categories = Category.query.filter_by(user_id=current_user.id).all()
    
    # Obliczenie statystyk
    stats = current_user.get_statistics()
    
    return render_template('task_list.html', 
                          tasks=tasks,
                          categories=categories,
                          stats=stats,
                          current_sort=sort,
                          current_category=category_id,
                          search_query=search_query,
                          current_status=status_filter)


# KALENDARZ

@task_bp.route('/calendar')
@login_required
def calendar():
    """
    Wyświetla kalendarz z zadaniami na danej dacie
    """
    import calendar as cal
    
    year = request.args.get('year', datetime.now().year, type=int)
    month = request.args.get('month', datetime.now().month, type=int)
    
    # Pobranie wszystkich zadań z datami
    tasks_with_dates = Task.query.filter(
        Task.user_id == current_user.id,
        Task.due_date.isnot(None)
    ).all()
    
    # Grupowanie zadań po datach
    tasks_by_date = {}
    for task in tasks_with_dates:
        date_str = task.due_date.strftime('%Y-%m-%d')
        if date_str not in tasks_by_date:
            tasks_by_date[date_str] = []
        tasks_by_date[date_str].append(task)
    
    # Generowanie dni kalendarza
    calendar_days = []
    
    # Pobranie pierwszego dnia miesiąca
    first_day = datetime(year, month, 1)
    start_weekday = first_day.weekday()  # 0=poniedziałek
    
    # Dni z poprzedniego miesiąca
    if start_weekday > 0:
        prev_month = month - 1 if month > 1 else 12
        prev_year = year if month > 1 else year - 1
        prev_month_last_day = cal.monthrange(prev_year, prev_month)[1]
        
        for i in range(start_weekday):
            day_num = prev_month_last_day - (start_weekday - 1 - i)
            day_date = datetime(prev_year, prev_month, day_num)
            calendar_days.append({
                'date': day_date,
                'month': prev_month
            })
    
    # Dni bieżącego miesiąca
    last_day = cal.monthrange(year, month)[1]
    for day in range(1, last_day + 1):
        day_date = datetime(year, month, day)
        calendar_days.append({
            'date': day_date,
            'month': month
        })
    
    # Dni z następnego miesiąca
    next_month_days = (42 - len(calendar_days))  # 6 rzędów * 7 dni
    for day in range(1, next_month_days + 1):
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1
        day_date = datetime(next_year, next_month, day)
        calendar_days.append({
            'date': day_date,
            'month': next_month
        })
    
    # Pobranie kategorii
    categories = Category.query.filter_by(user_id=current_user.id).all()
    
    # Obliczenie statystyk
    stats = current_user.get_statistics()
    
    return render_template('calendar.html',
                          year=year,
                          month=month,
                          calendar_days=calendar_days,
                          tasks_by_date=tasks_by_date,
                          categories=categories,
                          stats=stats,
                          now=datetime.now())

@task_bp.route('/task/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    # 1. Pobierz zadanie z bazy lub zwróć 404 jeśli nie istnieje
    task = Task.query.get_or_404(task_id)
    
    # 2. Odwróć obecny stan logiczny (True -> False / False -> True)
    task.is_completed = not task.is_completed
    
    try:
        # 3. Zapisz zmiany w bazie danych
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        flash('Wystąpił błąd podczas zmiany statusu.', 'danger')
    
    # 4. Przekieruj z powrotem na listę zadań
    return redirect(request.referrer or url_for('task.task_list'))