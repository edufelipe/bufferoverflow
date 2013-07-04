from django.forms import ModelForm, CharField, Textarea
from .models import Question, Tag, Answer


class QuestionForm(ModelForm):
    tags = CharField(max_length=255)

    class Meta:
        model = Question
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-block-level'

    def save(self, *args, **kwargs):
        q = super(QuestionForm, self).save(*args, **kwargs)
        for name in self.cleaned_data['tags'].split(u','):
            tag = Tag(question=q, name=name.strip())
            tag.save()
        return q


class AnswerForm(ModelForm):
    content = CharField(widget=Textarea(
        attrs={'class': 'input-block-level', 'rows': '5'}))
    class Meta:
        model = Answer
        fields = ['content']

