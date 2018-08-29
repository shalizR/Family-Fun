from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    content = models.CharField(
        verbose_name='content',
        max_length=100,
        blank=False
    )
    rating = models.IntegerField(
        verbose_name='rating',
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )
    date_created = models.DateTimeField(
        verbose_name='date_created',
        auto_now_add=True,
        null=True,
    )
    date_modified = models.DateTimeField(
        verbose_name='date_modified',
        auto_now=True,
        null=True,
    )
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    restaurant = models.ForeignKey(
        verbose_name='restaurant',
        on_delete=models.CASCADE,
        related_name='reviews',
        to='restaurant.Restaurant',
    )
    has_changing_table = models.NullBooleanField(
        verbose_name='has_changing_table',
    )
    place_for_stroller = models.NullBooleanField(
        verbose_name='place_for_stroller',
    )
    isNoisy = models.NullBooleanField(
        verbose_name='isNoisy',
    )
    friendly_waiting_staff = models.NullBooleanField(
        verbose_name='friendly_waiting_staff',
    )
    high_chair = models.NullBooleanField(
        verbose_name='high_chair',
    )
    are_there_steps = models.NullBooleanField(
        verbose_name='are_there_steps',
    )
    has_tablecloth = models.NullBooleanField(
        verbose_name='has_tablecloth',
    )
    has_quick_service = models.NullBooleanField(
        verbose_name='has_quick_service',
    )
    price_level = models.IntegerField(
        verbose_name='price_level',
        default=1,
        validators=[MaxValueValidator(4), MinValueValidator(1)],
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.content
