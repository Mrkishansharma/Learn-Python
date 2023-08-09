# crud/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
