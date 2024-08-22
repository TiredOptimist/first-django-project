document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('.container-settings-navbar a');

  links.forEach(link => {
    link.addEventListener('click', function(event) {
      // Предотвращаем стандартное действие ссылки
      event.preventDefault();

      // Удаляем класс 'active' со всех ссылок
      links.forEach(link => {
        link.classList.remove('active');
        link.classList.add('dis-active');
      });

      // Добавляем класс 'active' к нажатой ссылке
      this.classList.remove('dis-active');
      this.classList.add('active');

      // Переходим на URL, указанный в атрибуте href нажатой ссылки
      window.location.href = this.getAttribute('href');
    });
  });
});
