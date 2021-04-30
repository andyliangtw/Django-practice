from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_view),
    path('<int:id>/', views.singleVendor, name='vendor'),
]
