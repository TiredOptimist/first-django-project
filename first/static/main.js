function setTheme(theme) {
    document.documentElement.classList.remove('dark','lightstyle', 'pinkystyle', 'total-black');
    document.documentElement.classList.add(theme);
    localStorage.setItem('theme', theme);
}

document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        setTheme(savedTheme);
    }

    document.getElementById('dark').addEventListener('click', function() {
        setTheme('dark');
    });

    document.getElementById('light').addEventListener('click', function() {
        setTheme('lightstyle');
    });

    document.getElementById('pinky').addEventListener('click', function() {
        setTheme('pinkystyle');
    });

    document.getElementById('black').addEventListener('click', function() {
        setTheme('total-black');
    });
})