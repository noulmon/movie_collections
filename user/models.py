from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True, default='')
    last_name = models.CharField(_('Last name'), max_length=30, blank=True, default='')
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(
        _('Admin status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting account.'
        ),
    )
    is_delete = models.BooleanField(_('Delete'), default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username


class RequestCount(models.Model):
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'request_count'
        verbose_name = _('Request Count')
        verbose_name_plural = _('Request Counts')

    def __str__(self):
        return self.count.__str__()
