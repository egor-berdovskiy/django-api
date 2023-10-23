from django.db import models
from .dataclasses import UserType

class User(models.Model):
    type = models.CharField(max_length=32, default=UserType.user, validators=[UserType.validator])
    user_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=64)
    username = models.CharField(max_length=32, null=True)
    language = models.CharField(max_length=2, default='ru')
    register_time = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField(null=False, default=0)

    class Meta:
        ordering = ['pk']

    @property
    def is_admin(self) -> bool:
        return self.type == UserType.admin

    def __str__(self):
        return f'[{self.pk}] {self.user_id} | @{self.username}, language={self.language}, register_time={self.register_time} | {self.balance}'
