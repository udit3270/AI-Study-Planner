from django.db import models

from django.contrib.auth.models import User


class Subject(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    difficulty = models.IntegerField(
        default=1
    )

    target_days = models.IntegerField(
    default=30
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name


class StudySession(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    duration = models.IntegerField()

    completed = models.BooleanField(
        default=False
    )

    date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.subject.name}"
    
class StudyPlan(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    generated_plan = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} Plan"
    
class DailyStreak(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    current_streak = models.IntegerField(
        default=0
    )

    longest_streak = models.IntegerField(
        default=0
    )

    last_study_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):

        return f"{self.user.username} Streak"
    
