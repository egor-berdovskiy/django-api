from django.core.exceptions import ValidationError

class UserType:
    user = 'user'
    admin = 'admin'
    __all_values = [user, admin]

    @classmethod
    def validator(cls, value):
        if value not in cls.__all_values:
            raise ValidationError(f'{cls.__name__}: [{value}] not in {cls.__all_values}')
