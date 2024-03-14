from django.urls import path

from catalog.views import contacts, goods, CatalogListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('goods/<int:pk>', goods, name='goods'),
]
