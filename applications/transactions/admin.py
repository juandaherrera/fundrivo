from django.contrib import admin
from . import models

# --------------------------- Defaults ---------------------------

admin.site.register(models.Currency)
admin.site.register(models.AccountCategory)
admin.site.register(models.Account)