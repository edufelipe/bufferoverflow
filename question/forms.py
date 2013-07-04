from django.forms import ModelForm, CharField
from .models import Question, Tag


class QuestionForm(ModelForm):
    tags = CharField(max_length=255)

    class Meta:
        model = Question
        fields = ['title', 'content', 'tags']

    def save(self, *args, **kwargs):
        q = super(QuestionForm, self).save(*args, **kwargs)
        for name in self.cleaned_data['tags'].split(u','):
            tag = Tag(question=q, name=name.strip())
            tag.save()
        return q
