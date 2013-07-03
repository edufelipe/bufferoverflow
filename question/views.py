from django.template.response import TemplateResponse
from .models import Question


def home(request):
    questions = Question.objects.all()
    return TemplateResponse(request, 'question/list.html', {
        'questions': questions,
    })
