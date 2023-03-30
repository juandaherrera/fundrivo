from django.contrib import admin

class RestrictedModelAdmin(admin.ModelAdmin):
    """
    A ModelAdmin that restricts access to its model's objects based on the
    authenticated user. Only superusers can view all objects; non-superusers
    can only view objects that belong to them.
    """
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            # If the user is a superuser, show all objects.
            return qs
        else:
            # Otherwise, only show objects belonging to the current user.
            return qs.filter(_creator_user=request.user)
        

class RestrictedFieldsModelAdmin(admin.ModelAdmin):
    """
    A ModelAdmin that restricts access to certain fields of its model's objects based on the
    authenticated user. Only superusers can view all fields; non-superusers can only view fields
    that are not specified in the `restricted_fields` attribute.

    Usage example: 
    
    class AccountAdmin(RestrictedFieldsModelAdmin):
        def __init__(self, model, admin_site):
            super().__init__(model, admin_site, restricted_fields=['currency', 'name'])
    
    admin.site.register(models.Account, AccountAdmin)
    """

    def __init__(self, model, admin_site, restricted_fields=None):
        self.restricted_fields = restricted_fields or []
        super().__init__(model, admin_site)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj=obj)
        if not request.user.is_superuser:
            fields = [f for f in fields if f not in self.restricted_fields]
        return fields