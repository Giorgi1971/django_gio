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
