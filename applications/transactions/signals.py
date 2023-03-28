from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Currency

@receiver(post_migrate)
def create_currencies(sender, **kwargs):
    """
    This signal creates the objects defined below when a migration is performed and these objects do not exist.

    In addition, it brings the Representative Market Rate at the time of creation of the instances
    """

    if sender.name == 'applications.transactions':
        obj, created = Currency.objects.get_or_create(name='Pesos Colombianos', code='COP')
        if created:
            obj.update_trm()
        obj, created = Currency.objects.get_or_create(name='US Dollar', code='USD')
        if created:
            obj.update_trm()
