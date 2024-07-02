from django.core.management.base import BaseCommand
from django.apps import apps
import csv


class Command(BaseCommand):
    help = "import data to any model"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)
        parser.add_argument('model_name', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model = kwargs['model_name']
        print(model)
        print(file_path, model)
        if not model:
            print('no model available')

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model)
                break
            except LookupError as e:
                continue

        if model:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    model.objects.create(**row)
            self.stdout.write("your data successfully import in database")



