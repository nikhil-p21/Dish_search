from django.core.management.base import BaseCommand
from logs.models import restaurant
import csv

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv_data = restaurant(
                    # id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    # lat_long=row['lat_long'],
                    # full_details=row['full_details']
                )
                csv_data.save()
