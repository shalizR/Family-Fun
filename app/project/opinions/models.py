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
    helpful = models.NullBooleanField(
        verbose_name='helpful',
        default=False,
    )
    awesome = models.NullBooleanField(
        verbose_name='awesome',
        default=False,
    )
    random = models.NullBooleanField(
        verbose_name='random',
        default=False,
    )
