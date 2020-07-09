from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    questions = Question.objects.all()
    context = {
        'data': questions,
    }
    return render(request, 'polls/index.html', context)


def users(request):
    return HttpResponse('Aquí estan los usuarios')


def payments(request):
    return HttpResponse('Aquí están los pagos')
