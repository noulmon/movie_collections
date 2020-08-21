import uuid as uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.models import User


class BaseModel(models.Model):
    """
    model that will be inherited by all models to add common fields.
    """
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this should be treated as active. '
            'Unselect this instead of deleting.'
        ),
    )
    is_delete = models.BooleanField(_('delete'), default=False)
    modified_on = models.DateTimeField(auto_now=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UserMovieCollection(BaseModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_collections')

    class Meta:
        db_table = 'user_movie_collection'
        verbose_name = _('User Movie Collection')
        verbose_name_plural = _('User Movie Collections')

    def __str__(self):
        return self.uuid.__str__()


class CollectedMovie(models.Model):
    collection = models.ForeignKey(UserMovieCollection, on_delete=models.CASCADE, related_name='collection_movies',
                                   db_index=True)
    movie_uuid = models.CharField(max_length=100)

    class Meta:
        db_table = 'collected_movie'
        verbose_name = _('Collected Movie')
        verbose_name_plural = _('Collected Movies')
