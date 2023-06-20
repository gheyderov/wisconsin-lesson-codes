from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
User = get_user_model()


class Command(BaseCommand):
    help = "Used to delete users"
    requires_migrations_checks = True

    def handle(self, *args, **options):
        users = User.objects.filter(is_superuser = False)
        users.delete()