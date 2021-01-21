'''
    (
        (1, 'Fiction',),
        (2, 'Adventure',),
        (3, 'Fantasy',),
        (4, 'Poetry',),
        (5, 'Drama',),
        (6, 'Biography',),
        (7, 'Mystery',),
        )
'''

from django.db.models import IntegerChoices


class GenreChoices(IntegerChoices):
    Fiction = 1
    Adventure = 2
    Fantasy = 3
    Poetry = 4
    Drama = 5
    Biography = 6
    Mystery = 7


class CondChoices(IntegerChoices):
    New = 1
    Best = 2
    Good = 3
    Old = 4


class StatusChoices(IntegerChoices):
    Sale = 1
    Change = 2
    NotSale = 3
    Hidden = 4
