from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Главная'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Описание'}


class ProductTemplateView(TemplateView):
    extra_context = {'title': 'Контакты'}
    template_name = 'catalog/contacts.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')




