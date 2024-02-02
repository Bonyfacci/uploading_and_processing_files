import datetime
import os
import shutil
import logging

from celery import shared_task
from django.conf import settings
from magic import Magic

from file.models import File


logger = logging.getLogger(__name__)


@shared_task
def check_active_file():
    current_time = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    print(f'Время сервера: {current_time}')
    for file in File.objects.filter(processed=False):

        file_path = file.file.path
        logger.info(f"Processing file: {file_path}")

        # Определение MIME-типа файла с использованием python-magic
        mime = Magic()
        file_type = mime.from_file(file.file.path)

        # Определение папки для сохранения файла
        if 'text' in file_type:
            folder = 'text_files'
        elif 'image' in file_type:
            folder = 'image_files'
        else:
            folder = 'other_files'

        # Путь для сохранения файла в соответствующую папку
        save_path = os.path.join(settings.MEDIA_ROOT, folder, current_time, os.path.basename(file.file.name))
        print(f'Файл {os.path.basename(file.file.name)} обрабатывается')
        print(f'Файл является {folder}\n'
              f'Путь к файлу: {save_path}')

        # Перемещение файла в соответствующую папку
        try:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            shutil.move(file.file.path, save_path)
            file.file.name = os.path.join(folder, current_time, os.path.basename(file.file.name))
            print(f'Файл успешно перемещен!')
        except Exception as e:
            print(f'Ошибка при перемещении файла: {e}')

        # Обновление поля processed модели File на True после обработки файла
        file.processed = True
        file.save()

        print(f'Файл {file} обновлён!')
