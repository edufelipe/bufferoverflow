from django.conf.urls import patterns, url


urlpatterns = patterns('question.views',
    # Examples:
    url(r'^$', 'ask', name='ask'),
    url(r'^(?P<question>\d+)/$', 'detail', name='detail'),
    url(r'^tagged/(?P<tag>\w[\w-]*)/$', 'tagged',
        name='tagged'),
)
