from django.core.management.base import BaseCommand, CommandParser
from core.models import BlockedIps

class Command(BaseCommand):
    help = "Used to delete users"
    requires_migrations_checks = True

    def handle(self, *args, **options):
        ips = BlockedIps.objects.all()
        ips.delete()