from django.urls.conf import path
from . import views

app_name='images'
urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
]
