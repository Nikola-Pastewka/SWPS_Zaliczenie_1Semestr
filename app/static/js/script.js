// script.js - Funkcje JavaScript


//Inicjalizacja - wykonuje się po załadowaniu strony

document.addEventListener('DOMContentLoaded', function() {
    // Inicjalizuj tooltips Bootstrap
    initializeTooltips();

    // Inicjalizuj potwierdzenia akcji
    initializeConfirmations();
});


 //Dodaje potwierdzenia przed akcjami destrukcyjnymi (usuwanie, itp).
function initializeConfirmations() {
    // Pobierz wszystkie formularze usuwania
    const deleteForms = document.querySelectorAll('form[onsubmit*="confirm"]');

    deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const confirmed = confirm(this.getAttribute('onsubmit').match(/'([^']*)'/) ? 
                                     this.getAttribute('onsubmit').match(/'([^']*)'/) [1] : 
                                     'Na pewno?');
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });
}

 //Obsługuje zmianę statusu zadania (zaznaczenie checkboxa).
function toggleTaskStatus(taskId) {
    // Wyślij POST request do serwera
    fetch(`/task/${taskId}/toggle`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        // Sprawdź czy odpowiedź jest OK
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Jeśli sukces, odśwież stronę
        if (data.success) {
            location.reload();
        } else {
            console.error('Error:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Coś poszło nie tak!');
    });
}


 // Obsługuje zmianę statusu pilności zadania.

function toggleTaskUrgent(taskId) {
    // Wyślij POST request do serwera
    fetch(`/task/${taskId}/urgent`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Jeśli sukces, odśwież stronę
        if (data.success) {
            location.reload();
        } else {
            console.error('Error:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Coś poszło nie tak!');
    });
}


 //Formatuje datę w polskim formacie.
function formatDate(dateString) {
    const options = { 
        year: 'numeric', 
        month: '2-digit', 
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    };
    return new Date(dateString).toLocaleDateString('pl-PL', options);


 //Wyświetla toast (małe powiadomienie) na stronie.
function showToast(message, type = 'info', duration = 3000) {
    // Utwórz element toast
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; max-width: 300px;';
    toast.setAttribute('role', 'alert');
    
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Dodaj do strony
    document.body.appendChild(toast);
    
    // Automatycznie usuń po określonym czasie
    setTimeout(() => {
        toast.remove();
    }, duration);
}


 //Waliduje długość tekstu w polu input.
function validateInputLength(inputElement, maxLength) {
    inputElement.addEventListener('input', function() {
        if (this.value.length > maxLength) {
            this.value = this.value.substring(0, maxLength);
        }
    });
}

// Wyłącza przycisk submit na formularzu na czas wysyłania.
// Zapobiega podwójnemu wysłaniu formularza.
function disableFormOnSubmit(formElement) {
    formElement.addEventListener('submit', function() {
        const submitButton = this.querySelector('button[type="submit"]');
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Wysyłanie...';
        }
    });
}

// Eksportuj funkcje dla globalnego użytku
window.todoApp = {
    toggleTaskStatus,
    toggleTaskUrgent,
    formatDate,
    isTaskOverdue,
    showToast,
    validateInputLength,
    disableFormOnSubmit
}}
