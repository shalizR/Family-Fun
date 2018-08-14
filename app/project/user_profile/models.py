from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    location = models.CharField(
        verbose_name='location',
        null=True,
        max_length=100,
    )
    phone = models.CharField(
        verbose_name='phone',
        null=True,
        max_length=20,
    )
    joined_date = models.DateTimeField(
        verbose_name='joined_date',
        null=True,
    )
    profile_pic = models.ImageField(
        verbose_name='profile_picture',
        null=True,
        blank=True,
        upload_to='user_profile/',
    )

    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        return self.user.email
