from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'price'] # with help of this we can manage and see data very easily in admin penal
    search_fields = ['id', 'title', 'content'] # help to search data in admin penal using this fild
admin.site.register(Product, ProductAdmin) # with help of this we can manage models data in admin penal