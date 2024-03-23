from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория продукта')
    description = models.TextField(null=True, blank=True, verbose_name='описание продукта')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория продукта'
        verbose_name_plural = 'категории продуктов'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='название продукта')
    description = models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.image} {self.price} {self.created_at} {self.updated_at}'

    class Meta:
        verbose_name = 'название продукта'
        verbose_name_plural = 'названия продуктов'
        ordering = ('-name',)


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='версия №')
    version_name = models.CharField(max_length=150, verbose_name='имя версии')
    current_version = models.BooleanField(default=True, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product} {self.version_number} {self.version_name}'

    class Meta:
        verbose_name = 'связь'
        verbose_name_plural = 'связи'
