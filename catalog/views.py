from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView

from catalog.forms import ProductForm
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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:view_product', args=[self.kwargs.get('pk')])
