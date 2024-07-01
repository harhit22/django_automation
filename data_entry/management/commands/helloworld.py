from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "print the hello world"

    def handle(self, *args, **options):
        self.stdout.write('hello_world')
