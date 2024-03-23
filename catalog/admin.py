from django.contrib import admin

from catalog.models import Category, Product, ProductVersion


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'current_version',)