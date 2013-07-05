from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):

    def create_user(self, email, name, **extra_fields):
        """
        Creates and saves a User with the given email.
        """
        current_time = now()
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)

        if User.objects.filter(email__iexact=email):
            raise ValidationError('Email already in use.')

        user = self.model(email=email, name=name, last_login=current_time,
            date_joined=current_time, **extra_fields)

        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, email, name,  **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self.create_user(email, name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # User Data
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    avatar = models.FileField(upload_to='avatar', null=True, blank=True)

    # Django Requirements
    date_joined = models.DateTimeField(default=now)
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into django admin.')

    objects = UserManager()

    def get_full_name(self):
        return self.name or self.email

    def get_short_name(self):
        return self.get_full_name().split()[0]

