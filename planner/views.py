from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date, timedelta
from .models import (
    Subject,
    StudySession,
    StudyPlan,
    DailyStreak
)
from .forms import (
    SubjectForm,
    StudySessionForm
)
from .ai_generator import generate_schedule
from .forms import PomodoroForm
from django.http import JsonResponse


@login_required
def dashboard(request):

    subjects = Subject.objects.filter(
        user=request.user
    )

    sessions = StudySession.objects.filter(
        user=request.user
    ).order_by('-date')

    form = SubjectForm()

    session_form = StudySessionForm()

    if request.method == 'POST':

        if 'add_subject' in request.POST:

            form = SubjectForm(
                request.POST
            )

            if form.is_valid():

                subject = form.save(
                    commit=False
                )

                subject.user = request.user

                subject.save()

                return redirect(
                    'dashboard'
                )

        elif 'add_session' in request.POST:

            session_form = StudySessionForm(
                request.POST
            )

            if session_form.is_valid():

                session = session_form.save(
                    commit=False
                )

                session.user = request.user

                session.save()

                if session.completed:

                    streak, created = DailyStreak.objects.get_or_create(
                        user=request.user
                    )

                    today = date.today()

                    if streak.last_study_date is None:

                        streak.current_streak = 1

                    elif streak.last_study_date == today:

                        pass

                    elif streak.last_study_date == (
                        today - timedelta(days=1)
                    ):

                        streak.current_streak += 1

                    else:

                        streak.current_streak = 1

                    if (
                        streak.current_streak >
                        streak.longest_streak
                    ):

                        streak.longest_streak = (
                            streak.current_streak
                        )

                    streak.last_study_date = today

                    streak.save()

                return redirect(
                    'dashboard'
                )

    total_subjects = subjects.count()

    total_sessions = sessions.count()

    total_study_time = (
        sessions.aggregate(
            Sum('duration')
        )['duration__sum']
        or 0
    )

    today_study_time = (
        sessions.filter(
            date=date.today()
        ).aggregate(
            Sum('duration')
        )['duration__sum']
        or 0
    )

    streak, created = DailyStreak.objects.get_or_create(
        user=request.user
    )

    # =========================
    # CHART DATA
    # =========================

    subject_labels = []

    subject_minutes = []

    for subject in subjects:

        total_minutes = (
            StudySession.objects.filter(
                user=request.user,
                subject=subject
            ).aggregate(
                Sum('duration')
            )['duration__sum']
            or 0
        )

        subject_labels.append(
            subject.name
        )

        subject_minutes.append(
            total_minutes
        )

    context = {

        'subjects': subjects,

        'sessions': sessions,

        'form': form,

        'session_form': session_form,

        'total_subjects': total_subjects,

        'total_sessions': total_sessions,

        'total_study_time': total_study_time,

        'today_study_time': today_study_time,

        'current_streak': streak.current_streak,

        'longest_streak': streak.longest_streak,

        'subject_labels': subject_labels,

        'subject_minutes': subject_minutes,
    }

    return render(
        request,
        'planner/dashboard.html',
        context
    )


@login_required
def delete_subject(request, id):

    subject = get_object_or_404(
        Subject,
        id=id,
        user=request.user
    )

    subject.delete()

    return redirect(
        'dashboard'
    )


@login_required
def edit_subject(request, id):

    subject = get_object_or_404(
        Subject,
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        form = SubjectForm(
            request.POST,
            instance=subject
        )

        if form.is_valid():

            form.save()

            return redirect(
                'dashboard'
            )

    else:

        form = SubjectForm(
            instance=subject
        )

    return render(
        request,
        'planner/edit_subject.html',
        {
            'form': form
        }
    )


@login_required
def pomodoro(request):

    form = PomodoroForm(
        request.user
    )

    return render(
        request,
        'planner/pomodoro.html',
        {
            'form': form
        }
    )


@login_required
def ai_schedule(request):

    generated_plan = None

    subjects = Subject.objects.filter(
        user=request.user
    )

    if request.method == 'POST':

        study_hours = request.POST.get(
            'study_hours'
        )

        subject_id = request.POST.get(
            'subject_id'
        )

        subject = get_object_or_404(
            Subject,
            id=subject_id,
            user=request.user
        )

        subject_text = (
            f"""
            Subject: {subject.name}
            Difficulty: {subject.difficulty}/5
            Complete In: {subject.target_days} Days
            """
        )

        generated_plan = generate_schedule(
            subject_text,
            study_hours
        )

        StudyPlan.objects.create(
            user=request.user,
            generated_plan=generated_plan
        )

    previous_plans = StudyPlan.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'planner/ai_schedule.html',
        {
            'generated_plan': generated_plan,
            'previous_plans': previous_plans,
            'subjects': subjects
        }
    )

@login_required
def view_plan(request, id):

    plan = get_object_or_404(
        StudyPlan,
        id=id,
        user=request.user
    )

    return render(
        request,
        'planner/view_plan.html',
        {
            'plan': plan
        }
    )


@login_required
def delete_plan(request, id):

    plan = get_object_or_404(
        StudyPlan,
        id=id,
        user=request.user
    )

    plan.delete()

    return redirect(
        'ai_schedule'
    )

@login_required
def save_pomodoro_session(request):

    if request.method == "POST":

        subject_id = request.POST.get(
            "subject_id"
        )

        duration = request.POST.get(
            "duration"
        )

        subject = get_object_or_404(
            Subject,
            id=subject_id,
            user=request.user
        )

        StudySession.objects.create(
            user=request.user,
            subject=subject,
            duration=duration,
            completed=True
        )

        return JsonResponse(
            {
                "status": "success"
            }
        )

    return JsonResponse(
        {
            "status": "error"
        }
    )