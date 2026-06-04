from django.contrib import admin
from .models import (
    Subject,
    StudySession,
    StudyPlan,
    DailyStreak
)

admin.site.register(Subject)
admin.site.register(StudySession)
admin.site.register(StudyPlan)
admin.site.register(DailyStreak)


