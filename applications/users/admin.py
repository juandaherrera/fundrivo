from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            _('Custom info'), { #_ is an alias for the gettext_lazy function that allows to translate the arguments to the default language configured in settigns
            'fields': ('birthdate','country', 'app_permission')
            }
        ),
    )