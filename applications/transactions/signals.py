from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Currency

@receiver(post_migrate)
def create_currencies(sender, **kwargs):
    """
    This signal creates the objects defined below when a migration is performed and these objects do not exist
    """
    
    if sender.name == 'applications.transactions':
        Currency.objects.get_or_create(name='Pesos Colombianos', code='COP')
        Currency.objects.get_or_create(name='US Dollar', code='USD')
