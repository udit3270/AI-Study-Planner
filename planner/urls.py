from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'pomodoro/',
        views.pomodoro,
        name='pomodoro'
    ),

    path(
        'delete-subject/<int:id>/',
        views.delete_subject,
        name='delete_subject'
    ),

    path(
        'edit-subject/<int:id>/',
        views.edit_subject,
        name='edit_subject'
    ),

    path(
    'ai-schedule/',
    views.ai_schedule,
    name='ai_schedule'
    ),

    path(
    'view-plan/<int:id>/',
    views.view_plan,
    name='view_plan'
    ),

    path(
    'delete-plan/<int:id>/',
    views.delete_plan,
    name='delete_plan'
    ),

    path(
    'save-pomodoro-session/',
    views.save_pomodoro_session,
    name='save_pomodoro_session'
    ),

]