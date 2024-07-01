from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Greeting to user define in command"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='specific user name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write(f'hi {name}')