from django import forms
from .models import Subject, StudySession



class SubjectForm(forms.ModelForm):

    class Meta:

        model = Subject

        fields = [
            'name',
            'difficulty',
            'target_days'
        ]

class StudySessionForm(forms.ModelForm):

    class Meta:

        model = StudySession

        fields = [
            'subject',
            'duration',
            'completed'
        ]

from django import forms
from .models import Subject


class PomodoroForm(forms.Form):

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.none()
    )

    duration = forms.ChoiceField(
        choices=[
            (15, "15 Minutes"),
            (25, "25 Minutes"),
            (45, "45 Minutes"),
            (60, "60 Minutes"),
            (90, "90 Minutes"),
        ]
    )

    def __init__(self, user, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['subject'].queryset = Subject.objects.filter(
            user=user
        )