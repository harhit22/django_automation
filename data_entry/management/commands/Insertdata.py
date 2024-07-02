from django.core.management.base import BaseCommand
from data_entry.models import Student


class Command(BaseCommand):
    help = "inserting data to database"

    def handle(self, *args, **options):
        students_data = [
            {"name": "Arthur Morgan", "roll_no": 1, "age": 36},
            {"name": "John Marston", "roll_no": 2, "age": 26},
            {"name": "Dutch van der Linde", "roll_no": 3, "age": 44},
            {"name": "Sadie Adler", "roll_no": 4, "age": 25},
            {"name": "Charles Smith", "roll_no": 5, "age": 29},
            {"name": "Micah Bell", "roll_no": 6, "age": 39},
            {"name": "Javier Escuella", "roll_no": 7, "age": 30},
            {"name": "Bill Williamson", "roll_no": 8, "age": 37},
            {"name": "Hosea Matthews", "roll_no": 9, "age": 55},
            {"name": "Abigail Roberts", "roll_no": 10, "age": 22}
        ]

        for student in students_data:
            roll_no = student['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(**student)
                self.stdout.write(self.style.SUCCESS(f'Successfully inserted {student["name"]}'))
        self.stdout.write('data inserted successfully')
