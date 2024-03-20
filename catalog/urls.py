from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductTemplateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
