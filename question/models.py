from django.db import models


class Question(models.Model):
    """Represents a question someone asked."""
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    """Adds a shoprt label for questions."""
    question = models.ForeignKey(Question)
    name = models.SlugField()

    class Meta:
        unique_together = ('question', 'name')

    def __unicode__(self):
        return self.name
