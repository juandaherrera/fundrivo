from django.db import models
from applications.core.models import ModelClass
from django.utils import timezone

from datetime import datetime

from . import utils

class Currency(ModelClass):
    """
    This model is the representation of different currencies that we will use within the application. 
    """

    name = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    code = models.CharField(max_length=3, verbose_name='Código ISO 4217', unique=True)
    trm = models.DecimalField(max_digits=10, verbose_name='TRM Value', decimal_places=4, null=True, blank=True)
    trm_updated_at = models.DateTimeField(verbose_name='Last TRM Update', blank=True, null=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = "Currencies"
        ordering = ['code']

    def __str__(self):
        return self.code
    
    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)

    def update_trm(self):
        updated_at = timezone.now()

        if self.code == 'COP':
            trm_value = utils.trm(updated_at)

            if trm_value == 0:
                trm_value = self.trm
                updated_at = self.trm_updated_at

            self.trm = trm_value
            self.trm_updated_at = updated_at
            self.save()

        elif self.code == 'USD':
            self.trm = 1
            self.trm_updated_at = updated_at
            self.save()

        else:
            print(f'{self.code} is not supported')

    def get_old_trm(self, date):
        updated_at = datetime.strptime(date, '%Y-%m-%d')

        if self.code == 'COP':
            trm_value = utils.trm(updated_at)

            if trm_value == 0:
                return None

            return trm_value

        elif self.code == 'USD':
            return 1

        else:
            return None


# ------------------------------------------------------------- Accounts -------------------------------------------------------------

class AccountCategory(ModelClass):
    """
    This model is the representation of the account types that users can create.
    For example: savings account, credit cards, assets, liabilities.
    This model will only be accessible to the admin of the application. Users will not be able to create account categories.

    The icons have to be FontAwesome classes
    """
    name = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    icon = models.CharField(max_length=80, verbose_name='Icono (Fontawesome)', default='fa-solid fa-wallet')

    class Meta:
        verbose_name = 'Account Category'
        verbose_name_plural = "Account Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.icon = self.icon.lower().strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

