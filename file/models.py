from django.db import models


NULLABLE = {'null': True, 'blank': True}


class File(models.Model):
    """
    Модель файла
    """
    name = models.CharField(max_length=255, **NULLABLE, verbose_name="Наименование файла")
    file = models.FileField(upload_to="files/", verbose_name="Тип файла")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки файла")
    processed = models.BooleanField(default=False, verbose_name="Обработан")

    def __str__(self):
        return f'{self.name} - {self.file} - {self.uploaded_at}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ('name',)
