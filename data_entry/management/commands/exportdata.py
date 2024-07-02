import csv
import datetime
from django.apps import apps
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Export data from a given model"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        model_name = options['model_name']
        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if model:
            data = model.objects.all()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
            file_path = f'{model_name}-{timestamp}.csv'

            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([field.name for field in model._meta.fields])

                for dt in data:
                    writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

            self.stdout.write("Data export successfully")
        else:
            self.stdout.write(f"Model {model_name} not found.")
