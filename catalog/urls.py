from django.urls import path

from catalog.views import home, contacts, goods
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('goods/<int:pk>', goods, name='goods'),
]
