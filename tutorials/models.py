from django.db import models


# Create your models here.
from account.models import Account


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    published = models.BooleanField(default=False)
    registered_users = models.ManyToManyField(
        Account,
        related_name='registered_users',
        blank=True
    )

    def __str__(self):
        return '{}, there are ({}) users'.format(self.title, self.registered_users.all().count())
