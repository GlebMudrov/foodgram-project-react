from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField('Название тега',
        max_length=200,
        unique=True,
    )

    color = models.CharField('Цветовой HEX-код',
        max_length=7,
    )

    slug = models.SlugField('Слаг тега',
        max_length=200,
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Название ингредиента',
        max_length=200,
    )

    measurement_unit = models.CharField('Единицы измерения',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    pass