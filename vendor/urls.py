from django.urls import path

from . import views
from .apps import VendorConfig

app_name = VendorConfig.name
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_view, name='create'),
    path('<int:id>/', views.singleVendor, name='id'),
]
