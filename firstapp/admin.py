from django.contrib import admin

# Register your models here.
from .models import FirstModel

class FirstModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','content'] # with help of this we can manage and see data very easily in admin penal
    search_fields = ['title', 'content'] # help to search data in admin penal using this fild
admin.site.register(FirstModel, FirstModelAdmin) # with help of this we can manage models data in admin penal

