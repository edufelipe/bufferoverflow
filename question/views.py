from django.template.response import TemplateResponse
from django.shortcuts import redirect

from .models import Question
from .forms import QuestionForm


def home(request):
    questions = Question.objects.all()
    return TemplateResponse(request, 'question/list.html', {
        'questions': questions,
    })

def detail(request, question):
    question = Question.objects.get(pk=question)
    return TemplateResponse(request, 'question/detail.html', {
        'question': question,
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
            return redirect('home')

    return TemplateResponse(request, 'question/ask.html', {
        'form': form,
    })