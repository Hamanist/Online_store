from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    object_list = Product.objects.all()
    context = {
        'objects': object_list,
        'title': 'Главная',
    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}\n{message}')

    return render(request, 'catalog/contacts.html', context)


def goods(request, pk):
    object_list_goods = Product.objects.get(pk=pk)
    context = {
        'object': object_list_goods,
        'title': 'Описание',
    }
    return render(request, 'catalog/goods.html', context)
