from django.contrib import admin
from . import models

from django.db.models import Q

# --------------------------- Personalized ---------------------------
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'trm', 'trm_updated_at')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', '_creator_user', 'category', 'name', 'currency', 'balance','_created_at', '_updated_at')
    ordering = ('_creator_user', 'name')
    search_fields = ('name', 'currency', '_creator_user__username', 'category__name') # Campos por los que se puede buscar
    list_filter = ('_creator_user', 'currency', 'name') # Campos por los que se puede filtrar



class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', '_creator_user', 'name', 'description', 'icon', 'parent_category', '_created_at')
    ordering = ('_creator_user', 'name')
    search_fields = ('name', 'description', '_creator_user__username', 'parent_category__name') # Campos por los que se puede buscar
    list_filter = ('_creator_user', 'parent_category', 'name') # Campos por los que se puede filtrar


# --------------------------- Defaults ---------------------------

admin.site.register(models.AccountCategory)

admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.ExpenseCategory, ExpenseCategoryAdmin)
