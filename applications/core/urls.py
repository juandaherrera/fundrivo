from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'Core'

urlpatterns = [
    path('', views.Home.as_view(), name="home"),

    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'), name='logout'),

    path('no_privileges/', views.NoPrivilegesTemplate.as_view(), name="no_privileges"),
]