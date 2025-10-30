from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_click/', views.register_click, name='register_click'),
]
