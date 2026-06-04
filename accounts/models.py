from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    study_hours_per_day = models.IntegerField(
        default=4
    )

    preferred_start_time = models.TimeField(
        null=True,
        blank=True
    )

    preferred_end_time = models.TimeField(
        null=True,
        blank=True
    )

    def __str__(self):

        return self.user.username