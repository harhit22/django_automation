import csv

from django.core.management.base import BaseCommand
from data_entry.models import Student


# command we need is python manage.py file_path
class Command(BaseCommand):
    help = "This command is used for import data from csv to database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="please specify file path only csv allowed")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Student.objects.create(**row)
        self.stdout.write("your data successfully import in database")

