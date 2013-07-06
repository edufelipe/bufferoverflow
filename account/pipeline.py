from django.core.files.base import ContentFile

from urllib2 import urlopen, HTTPError

from .models import User


def get_avatar(user, response, *args, **kwargs):
    if kwargs.get('is_new', False) and response.get('picture'):
        try:
            avatar = urlopen(response['picture'])
            user.avatar.save(str(user.pk) + u'.jpg',
                ContentFile(avatar.read()))
            user.save()
        except HTTPError:
            pass

    return {}


def create_user(user, request, details, *args, **kwargs):
    """Create user and profile."""
    if user:
        return {'user': user}

    email = details.get('email')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = User.objects.create_user(email=email,
            name=details.get('fullname'))

    return {
        'user': user,
        'is_new': True
    }
