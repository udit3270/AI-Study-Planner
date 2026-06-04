from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.note_list,
        name='note_list'
    ),

    path(
        'delete/<int:id>/',
        views.delete_note,
        name='delete_note'
    ),
]