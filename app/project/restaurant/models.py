from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    CATEGORIES = [
        ('restaurant', 'Restaurant'),
        ('fast_food', 'Fast_Food'),
        ('cafe', 'Cafe'),
    ]
    name = models.CharField(
        verbose_name='name',
        max_length=100,
    )
    category = models.CharField(
        verbose_name='category',
        max_length=100,
        choices=CATEGORIES,
    )
    country = models.CharField(
        verbose_name='country',
        max_length=100,
        blank=True,
        null=True,
    )
    street = models.CharField(
        verbose_name='street',
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name='city',
        max_length=100,
        blank=True,
        null=True,
    )
    ZIP = models.CharField(
        verbose_name='ZIP',
        max_length=10,
        blank=True,
        default='0000'
    )
    website = models.CharField(
        verbose_name='website',
        max_length=100,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        verbose_name='phone',
        max_length=20,
        blank=True,
        null=True,
    )
    opening_hours = models.DateTimeField(
        verbose_name='opening_hours',
        null=True,
    )
    image = models.ImageField(
        verbose_name='restaurant picture',
        upload_to='restaurant/',
        blank=True,
        null=True,
    )
    credit_card = models.NullBooleanField(
        verbose_name='credit_card',
        default=False,
    )
    take_reservation = models.NullBooleanField(
        verbose_name='take_reservation',
        default=False,
    )
    kids_menu = models.NullBooleanField(
        verbose_name='kids_menu',
        default=False,
    )
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='restaurants',
    )

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
