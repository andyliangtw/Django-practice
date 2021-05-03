from django.urls import path

from .views import VendorListView, VendorDetailView, VendorCreateView, VendorUpdateView
from .apps import VendorConfig

app_name = VendorConfig.name
urlpatterns = [
    path('', VendorListView.as_view(), name='index'),
    path('create/', VendorCreateView.as_view(), name='create'),
    path('<int:pk>/', VendorDetailView.as_view(), name='pk'),
    path('<int:pk>/update/', VendorUpdateView.as_view(), name='update'),
]
