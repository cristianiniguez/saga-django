from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    return HttpResponse(f'You are seeing the question number {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are seeing the results of question number {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting for question number {question_id}')
