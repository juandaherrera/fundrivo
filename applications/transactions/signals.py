from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Currency, AccountCategory
from .input_data import category_descriptions, category_icons

@receiver(post_migrate)
def create_defeault_instances(sender, **kwargs):
    """
    This signal creates the objects defined below when a migration is performed and these objects do not exist.

    In addition, it brings the Representative Market Rate at the time of creation of the instances
    """

    if sender.name == 'applications.transactions':
        # --------------- Default Transactions ---------------
        obj, created = Currency.objects.get_or_create(name='Pesos Colombianos', code='COP')
        if created:
            obj.update_trm()
        obj, created = Currency.objects.get_or_create(name='US Dollar', code='USD')
        if created:
            obj.update_trm()

        # --------------- Default Account Categories ---------------
        AccountCategory.objects.get_or_create(name='Cuenta corriente', description=category_descriptions['Cuenta corriente'], icon=category_icons['Cuenta corriente'])
        AccountCategory.objects.get_or_create(name='Tarjeta de crédito', description=category_descriptions['Tarjeta de crédito'], icon=category_icons['Tarjeta de crédito'])
        AccountCategory.objects.get_or_create(name='Activo', description=category_descriptions['Activo'], icon=category_icons['Activo'])
        AccountCategory.objects.get_or_create(name='Pasivo', description=category_descriptions['Pasivo'], icon=category_icons['Pasivo'])