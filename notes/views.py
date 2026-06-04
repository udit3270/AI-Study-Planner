from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteForm


@login_required
def note_list(request):

    notes = Note.objects.filter(
        user=request.user
    )

    form = NoteForm()

    if request.method == 'POST':

        form = NoteForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            note = form.save(commit=False)

            note.user = request.user

            note.save()

            return redirect('note_list')

    return render(
        request,
        'notes/note_list.html',
        {
            'notes': notes,
            'form': form
        }
    )


@login_required
def delete_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        user=request.user
    )

    note.delete()

    return redirect('note_list')