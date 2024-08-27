let currentThemeName = localStorage.getItem('theme') || 'light';

const themeButtons = document.querySelectorAll('.button-theme');

themeButtons.forEach(button => {
    button.addEventListener('click', () => {
        const themeName = button.id;
        switch(themeName) {
            case 'dark':
                applyTheme('dark');
                break;
            case 'light':
                applyTheme('light');
                break;
            case 'pinky':
                applyTheme('pinkystyle');
                break;
            case 'black':
                applyTheme('dark'); // Используем темную тему для черной темы
                break;
        }
    });
});

function applyTheme(theme) {
    localStorage.setItem('theme', theme);
    
    document.body.classList.remove('lightstyle', 'darkstyle', 'pinkystyle');
    document.body.classList.add(theme);

    const themeElement = document.querySelector(`#${theme}`);
    if (themeElement) {
        themeElement.style.backgroundColor = '#007bff';
    }
}

// Инициализация темы при загрузке страницы
applyTheme(currentThemeName);
