from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from applications.users.models import CustomUser

from .models import Currency, AccountCategory, ExpenseCategory
from .input_data import currency_instances, account_category_instaces, default_expense_categories

@receiver(post_migrate)
def create_defeault_instances(sender, **kwargs):
    """
    This signal creates the objects defined below when a migration is performed and these objects do not exist.

    In addition, it brings the Representative Market Rate at the time of creation of the instances
    """

    if sender.name == 'applications.transactions':
        # --------------- Default Transactions ---------------
        for c in currency_instances:
            obj, created = Currency.objects.get_or_create(code=c, name=currency_instances[c])
            if created:
                obj.update_trm()

        # --------------- Default Account Categories ---------------
        for ac in account_category_instaces:
            AccountCategory.objects.get_or_create(
                name=ac, 
                description=account_category_instaces[ac]['description'], 
                icon=account_category_instaces[ac]['icon']
            )


@receiver(post_save, sender=CustomUser)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        # Create default ExpenseCategory instances
        for category_data in default_expense_categories:
            category_data['_creator_user'] = instance
            ExpenseCategory.objects.create(**category_data)
