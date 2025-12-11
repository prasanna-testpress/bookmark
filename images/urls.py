from django.urls.conf import path
from . import views

app_name='images'
urlpatterns = [
    path('create/', views.image_create, name='create'),
]
