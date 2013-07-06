from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'question.views.home', name='home'),
    url(r'^question/', include('question.urls')),
    # Add social_auth URLs
    url(r'', include('social_auth.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Serve files belonging to users (such as their avatar)
urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
