from django.apps import AppConfig


class FileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file'
    verbose_name = 'Загрузка и обработка файлов'
