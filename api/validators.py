import datetime

from django.core.exceptions import ValidationError


def year_validation(value):
    if value > datetime.datetime.now().year:
        raise ValidationError(
            ('%(value)s is not acceptable!'),
            params={'value': value},
        )
