from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        if not User.objects.filter(username='admin').exists():
            User.objects.create_user(
                username='admin',
                email='admin@mail.com',
                password='admin',
                is_staff=True,
                is_active=True,
                is_superuser=True
            )
        else:
            print(f'Суперпользователь уже создан!')
