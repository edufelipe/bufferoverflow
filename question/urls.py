from django.conf.urls import patterns, url


urlpatterns = patterns('question.views',
    # Examples:
    url(r'^$', 'ask', name='ask'),
)
