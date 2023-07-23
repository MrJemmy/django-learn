from django.urls import path

from .views import (
    show_data, create_entry, show_data_slug
)

app_name='firstapp'
urlpatterns = [
    path('', show_data),
    path('create/', create_entry, name='create'),
    path('<int:id>/', show_data, name='show'),
    path('<slug:slug>/', show_data_slug, name='show-slug'),
]
