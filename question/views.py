from django.template.response import TemplateResponse
from django.shortcuts import redirect

from .models import Question
from .forms import QuestionForm


def home(request):
    questions = Question.objects.all()
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