from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class ModelClass(models.Model):
    """
    Project model class
    """

    _deleted = models.BooleanField(verbose_name='Deleted', default=False)
    _created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    _updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    _creator_user = UserForeignKey(verbose_name='Creator user', auto_user_add=True, related_name='+')
    _updater_user = UserForeignKey(verbose_name='Updater user', auto_user=True, related_name='+')

    class Meta:
        abstract = True