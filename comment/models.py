from django.db import models
from datetime import datetime


# Create your models here.
from account.models import Account


# TODO: there should be a constraint where the person needs to be registered in tuto in order to comment
from tutorials.models import Tutorial


class Comment(models.Model):
    time = models.DateTimeField(default=datetime.now(), blank=True, editable=False)
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    comment = models.TextField(blank=False)

    tutorial = models.ForeignKey(
        Tutorial,
        on_delete=models.CASCADE,
        related_name='tutorial_comments',
        blank=True,
        null=True,
    )

    def __str__(self):
        return '"{}" at time {} by {}'.format(self.comment, self.time, self.user.email)
