from django.urls import path, include
from . import views

app_name='account'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
      path('register/', views.register, name='register'),

    # Edit profile
    path('edit/', views.edit, name='edit'),

    # Authentication URLs (login, logout, password reset, etc)
    path('', include('django.contrib.auth.urls')),

    path('users/', views.user_list, name='user_list'),
      path('users/follow/', views.user_follow, name='user_follow'),
    
    path('users/<username>/', views.user_detail, name='user_detail'),
  
]
