from django.apps import AppConfig


class PagesConfig(AppConfig):
    """Конфигурация приложения Страницы."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
    verbose_name = 'Страницы'
