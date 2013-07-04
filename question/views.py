from django.contrib import messages
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def home(request):
    questions = Question.objects.all()
    return TemplateResponse(request, 'question/list.html', {
        'questions': questions,
    })


def detail(request, question):
    form = AnswerForm()
    question = Question.objects.get(pk=question)

    if request.method == 'POST':
        form = AnswerForm(request.POST,
            instance=Answer(question=question))
        if form.is_valid():
            form.save()
            form = AnswerForm()

    return TemplateResponse(request, 'question/detail.html', {
        'question': question,
        'form': form,
    })


def tagged(request, tag):
    questions = Question.objects.filter(tag__name=tag)
    return TemplateResponse(request, 'question/list.html', {
        'questions': questions,
    })


def ask(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                'Question Asked Successfully.')
            return redirect('home')

    return TemplateResponse(request, 'question/ask.html', {
        'form': form,
    })