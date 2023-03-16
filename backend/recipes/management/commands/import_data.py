import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient

FILE_PATH = 'data/ingredients.csv'


class Command(BaseCommand):
    help = 'Импорт ингредиентов из csv-файла в базу данных.'

    def handle(self, *args, **options):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = csv.reader(file)
            for row in data:
                name, measurement_unit = row
                Ingredient.objects.get_or_create(
                    name=name,
                    measurement_unit=measurement_unit
                )
        print('Загрузка завершена.')
