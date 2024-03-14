from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

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



# def home(request):
#     object_list = Product.objects.all()
#     context = {
#         'objects': object_list,
#         'title': 'Главная',
#     }
#     return render(request, 'catalog/product_list.html', context=context)


# def contacts(request):
#     context = {
#         'title': 'Контакты',
#     }
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} {phone}\n{message}')
#
#     return render(request, 'catalog/contacts.html', context)

# def goods(request, pk):
#     object_list_goods = Product.objects.get(pk=pk)
#     context = {
#         'object': object_list_goods,
#         'title': 'Описание',
#     }
#     return render(request, 'catalog/product_detail.html', context)
