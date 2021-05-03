from django.urls import path

from . import views
from .apps import WelcomeConfig

app_name = WelcomeConfig.name
urlpatterns = [
    path('', views.index, name='index'),
]
