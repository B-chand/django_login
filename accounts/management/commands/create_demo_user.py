from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a demo user (username: admin, password: admin12345) if it does not exist.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        password = 'admin12345'

        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Created demo user: admin / admin12345'))
            return

        if not user.check_password(password):
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.WARNING('Demo user existed; password reset to admin12345'))
        else:
            self.stdout.write('Demo user already exists: admin / admin12345')
