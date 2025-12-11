from django.urls import path, include
from . import views

app_name='account'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Authentication URLs (login, logout, password reset, etc)
    path('', include('django.contrib.auth.urls')),
]
