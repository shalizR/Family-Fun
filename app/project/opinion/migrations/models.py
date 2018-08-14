from django.conf import settings
from django.db import models

from ..review.models import Review


class Opinion(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='opinions',
    )
    review = models.ForeignKey(
        verbose_name='review',
        to=Review,
        on_delete=models.CASCADE,
        related_name='opinions',
    )
    date_created = models.DateTimeField(
        verbose_name='date_created',
        null=True,
    )
    date_modified = models.DateTimeField(
        verbose_name='date_modified',
        null=True,
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.date_created
