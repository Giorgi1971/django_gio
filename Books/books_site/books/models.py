from django.db import models

# Create your models here.
from django.db import models
from books.choices import GenreChoices


class BookModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Name")
    created = models.DateTimeField(verbose_name="Added Date/Time", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated Date/Time", auto_now=True)
    quantity = models.PositiveSmallIntegerField(verbose_name="Stock", default=1)
    author = models.ForeignKey(to='store.AuthorModel', on_delete=models.PROTECT)
    genre = models.PositiveSmallIntegerField("Gender", choices=GenreChoices.choices, default=GenreChoices.Other)
    condition = models.PositiveSmallIntegerField("Gender", choices=GenreChoices.choices, default=GenreChoices.Other)
    models.PositiveSmallIntegerField("Gender", choices=GenreChoices.choices, default=GenreChoices.Other)

    class Meta:
        # unique_together = ('name', 'author')
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name

    def get_quantity(self):
        return f'რაოდენობაშია: {self.quantity}'


class AuthorModel(models.Model):
    full_name = models.CharField("Full Name", max_length=255)
    age = models.PositiveSmallIntegerField("Age")
    gender = models.PositiveSmallIntegerField("Gender", choices=GenderChoices.choices, default=GenderChoices.Other)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.full_name

    def get_info(self):
        return f'Age: {self.age}'
