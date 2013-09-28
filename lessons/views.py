# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from datetime import datetime

from lessons.models import Lesson


def index(request):
    lessons = Lesson.objects.filter(time__gte=datetime.now())
    return render(request, 'lessons/index.html', {'lessons': lessons})

@login_required(login_url='/account/login')
def book(request, lesson_pk):
    try:
        lesson = Lesson.objects.get(pk=lesson_pk)
    except Lesson.DoesNotExist:
        return Http404
    if lesson.remaining_num > 0:
        lesson.users.add(request.user)
        lesson.save()
    return redirect('index')

@login_required(login_url='/account/login')
def cancel_lesson(request, lesson_pk):
    try:
        lesson = Lesson.objects.get(pk=lesson_pk)
    except Lesson.DoesNotExist:
        return Http404
    lesson.users.remove(request.user)
    lesson.save()
    return redirect('index')

