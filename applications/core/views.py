from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.

class MixinFormInvalid:
    """
    Mixin validator of forms that come from a modal window
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class NoPrivileges(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    """
    This class controls the login and permissions that users have. Also, it inherits the MixinFormInvalid
    """
    login_url = 'Core:login'

    #Para que no se ponga la pantalla en blanco
    raise_exception = False
    
    redirect_field_name="redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='Core:no_privileges'
        return HttpResponseRedirect(reverse_lazy(self.login_url))
    

# ------------------------------------------------ GENERIC VIEWS ------------------------------------------------


class BaseCreateView(SuccessMessageMixin, NoPrivileges, CreateView):
    """
    Creation model view. From this view it will inherit all other creation views.
    """

    success_message="Registro agregado con éxito"
    
    def form_valid(self, form):
        form.instance._creator_user = self.request.user
        return super().form_valid(form)

class BaseUpdateView(SuccessMessageMixin, NoPrivileges, UpdateView):
    """
    Update model view. From this view it will inherit all other update views.
    """

    success_message="Registro actualizado con éxito"
    
    def form_valid(self, form):
        form.instance._updater_user = self.request.user
        return super().form_valid(form)
    
    

# ------------------------------------------------ CORE VIEWS ------------------------------------------------


class Home(TemplateView):
    """
    Home page
    """
    template_name = 'core/home.html'
    login_url = reverse_lazy('Core:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    

class NoPrivilegesTemplate(LoginRequiredMixin,TemplateView):
    """
    This view is for users that have no privileges to access a view
    """
    login_url = reverse_lazy('Core:login')
    template_name = 'core/no_privileges.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Sin permisos'
        context['entity'] = 'Sin permisos'
        return context
