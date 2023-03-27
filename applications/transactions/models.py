from django.db import models
from applications.core.models import ModelClass
# Create your models here.

class Currency(ModelClass):
    """
    This model is the representation of different currencies that we will use within the application. 
    """
    
    name = models.CharField(max_length=80, verbose_name='Nombre', unique=True)
    code = models.CharField(max_length=3, verbose_name='Código ISO 4217', unique=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = "Currencies"
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code
    