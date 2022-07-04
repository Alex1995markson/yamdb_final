from django.core.exceptions import ValidationError
from django.utils import timezone


def validation_of_the_year(year):
    current_year = timezone.now().year
    if year > current_year:
        raise ValidationError(
            'Указанный год не может быть больше текущего')
